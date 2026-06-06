from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from antlr4 import CommonTokenStream, FileStream
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees

from compiler.errors import CompilerError
from generated.CompiladorLexer import CompiladorLexer
from generated.CompiladorParser import CompiladorParser


ATRIBUTOS_TOKEN = {
    ("OPAD", "+"): "MAIS",
    ("OPAD", "-"): "MENOS",
    ("OPMULT", "*"): "VEZES",
    ("OPMULT", "/"): "DIV",
    ("OPLOG", "OR"): "OR",
    ("OPLOG", "AND"): "AND",
    ("OPNEG", "~"): "NEG",
    ("OPREL", "<"): "MENOR",
    ("OPREL", "<="): "MENIG",
    ("OPREL", ">"): "MAIOR",
    ("OPREL", ">="): "MAIG",
    ("OPREL", "=="): "IGUAL",
    ("OPREL", "<>"): "DIFER",
}


class TratadorDeErro(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if offendingSymbol is not None and (offendingSymbol.text or "").upper() == "END":
            entrada = recognizer.getInputStream()
            indice_anterior = offendingSymbol.tokenIndex - 1
            anterior = entrada.get(indice_anterior) if indice_anterior >= 0 else None

            if anterior is not None and anterior.type == CompiladorParser.BEGIN:
                raise CompilerError("Erro sintatico: bloco BEGIN END deve possuir ao menos um comando.")

            if anterior is not None and anterior.type == CompiladorParser.PVIG:
                raise CompilerError("Erro sintatico: ponto e virgula extra apos o ultimo comando.")

        raise CompilerError(f"Erro sintatico na linha {line}, coluna {column}: {msg}")


def validar_token(token, nomes_simbolicos):
    tipo = nomes_simbolicos[token.type]
    texto = token.text or ""

    if tipo == "ERROR_CHAR":
        raise CompilerError(
            f"Erro lexico na linha {token.line}, coluna {token.column}: simbolo invalido '{texto}'."
        )

    if tipo == "ID" and len(texto) > 16:
        raise CompilerError(
            f"Erro lexico na linha {token.line}, coluna {token.column}: identificador '{texto}' excede o limite de 16 caracteres."
        )

    if tipo == "UNCLOSED_STRING":
        raise CompilerError(
            f"Erro lexico na linha {token.line}, coluna {token.column}: cadeia nao fechada."
        )

    if tipo == "CTE" and int(texto) > 32768:
        raise CompilerError(
            f"Erro lexico na linha {token.line}, coluna {token.column}: constante inteira fora do limite de 2 bytes."
        )


def descrever_token(token, nomes_simbolicos):
    tipo = nomes_simbolicos[token.type]
    texto = token.text or ""

    if tipo == "ID":
        atributo = texto[:16]
    elif tipo == "CTE":
        atributo = texto
    elif tipo == "CADEIA":
        atributo = texto[1:-1]
    else:
        atributo = ATRIBUTOS_TOKEN.get((tipo, texto.upper()), "-")

    return f"{texto:<18} tipo={tipo:<10} atributo={atributo}"


def validar_cadeias(texto: str):
    dentro_cadeia = False
    linha_inicio = 1
    coluna_inicio = 0
    linha = 1
    coluna = 0
    indice = 0

    while indice < len(texto):
        caractere = texto[indice]

        if not dentro_cadeia and texto[indice : indice + 2] == "//":
            while indice < len(texto) and texto[indice] not in "\r\n":
                indice += 1
                coluna += 1
            continue

        if caractere == '"' and not dentro_cadeia:
            dentro_cadeia = True
            linha_inicio = linha
            coluna_inicio = coluna
        elif caractere == '"' and dentro_cadeia:
            dentro_cadeia = False
        elif caractere in "\r\n" and dentro_cadeia:
            raise CompilerError(
                f"Erro lexico na linha {linha_inicio}, coluna {coluna_inicio}: cadeia nao fechada."
            )

        if caractere == "\n":
            linha += 1
            coluna = 0
        elif caractere != "\r":
            coluna += 1

        indice += 1

    if dentro_cadeia:
        raise CompilerError(
            f"Erro lexico na linha {linha_inicio}, coluna {coluna_inicio}: cadeia nao fechada."
        )


def validar_comandos_compostos(arvore):
    for cmd_comp in _encontrar_contextos(arvore, CompiladorParser.CmdCompContext):
        lista = cmd_comp.listCmd()
        if lista is None:
            raise CompilerError("Erro sintatico: bloco BEGIN END deve possuir ao menos um comando.")

        quantidade_comandos = len(lista.cmd())
        quantidade_separadores = len(lista.PVIG())
        if quantidade_separadores != quantidade_comandos - 1:
            raise CompilerError("Erro sintatico: ponto e virgula extra apos o ultimo comando.")


def _encontrar_contextos(contexto, tipo_contexto):
    if isinstance(contexto, tipo_contexto):
        yield contexto

    for filho in getattr(contexto, "children", []) or []:
        yield from _encontrar_contextos(filho, tipo_contexto)


def compilar_arquivo(caminho_fonte: Path):
    validar_cadeias(caminho_fonte.read_text(encoding="utf-8"))
    entrada = FileStream(str(caminho_fonte), encoding="utf-8")
    lexer = CompiladorLexer(entrada)
    lexer.removeErrorListeners()
    lexer.addErrorListener(TratadorDeErro())

    tokens = CommonTokenStream(lexer)
    tokens.fill()

    print("=== TOKENS RECONHECIDOS ===")
    for token in tokens.tokens:
        if token.type == -1:
            continue
        validar_token(token, lexer.symbolicNames)
        print(descrever_token(token, lexer.symbolicNames))

    parser = CompiladorParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(TratadorDeErro())
    arvore = parser.programa()
    validar_comandos_compostos(arvore)

    print("\n=== ARVORE SINTATICA ===")
    print(Trees.toStringTree(arvore, None, parser))


def main():
    if len(sys.argv) != 2:
        print("Uso: python src/main.py <arquivo-fonte>")
        sys.exit(1)

    caminho_fonte = Path(sys.argv[1]).resolve()
    if not caminho_fonte.exists():
        print(f"Arquivo nao encontrado: {caminho_fonte}")
        sys.exit(1)

    try:
        compilar_arquivo(caminho_fonte)
    except Exception as exc:
        print(exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
