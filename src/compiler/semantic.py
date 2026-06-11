from collections import OrderedDict
from dataclasses import dataclass
from typing import Optional

from compiler.errors import CompilerError
from generated.CompiladorVisitor import CompiladorVisitor


TIPO_INTEGER = "INTEGER"
TIPO_BOOLEAN = "BOOLEAN"
TIPO_STRING = "STRING"
LIMITE_ID = 16
MIN_INTEGER = -32768
MAX_INTEGER = 32767


def normalizar_identificador(texto: str) -> str:
    return texto[:LIMITE_ID]


@dataclass
class EntradaSimbolo:
    nome: str
    tipo: str
    deslocamento: int
    escopo: int

    @property
    def tamanho(self):
        return tamanho_tipo(self.tipo)


def tamanho_tipo(tipo):
    if tipo == TIPO_INTEGER:
        return 2
    if tipo == TIPO_BOOLEAN:
        return 1
    return 256


class EscopoSimbolos:
    def __init__(self, nivel=0, pai=None):
        self.nivel = nivel
        self.pai = pai
        self.simbolos = OrderedDict()

    def declarar(self, nome, tipo, deslocamento):
        if nome in self.simbolos:
            return None

        entrada = EntradaSimbolo(nome, tipo, deslocamento, self.nivel)
        self.simbolos[nome] = entrada
        return entrada

    def buscar(self, nome):
        if nome in self.simbolos:
            return self.simbolos[nome]
        if self.pai is not None:
            return self.pai.buscar(nome)
        return None


class TabelaSimbolos:
    def __init__(self):
        self.raiz = EscopoSimbolos()
        self.atual = self.raiz
        self._escopos = [self.raiz]
        self._proximo_deslocamento = 0

    def abrir_escopo(self):
        escopo = EscopoSimbolos(len(self._escopos), self.atual)
        self._escopos.append(escopo)
        self.atual = escopo

    def fechar_escopo(self):
        if self.atual.pai is not None:
            self.atual = self.atual.pai

    def declarar(self, nome, tipo):
        entrada = self.atual.declarar(nome, tipo, self._proximo_deslocamento)
        if entrada is not None:
            self._proximo_deslocamento += entrada.tamanho
        return entrada

    def buscar(self, nome):
        return self.atual.buscar(nome)

    def entradas(self):
        resultado = []
        for escopo in self._escopos:
            resultado.extend(escopo.simbolos.values())
        return resultado

    def items(self):
        return [(entrada.nome, entrada.tipo) for entrada in self.entradas()]


class AnalisadorSemantico(CompiladorVisitor):
    def __init__(self):
        self.tabela_simbolos = TabelaSimbolos()
        self._nivel_cmd_comp = 0

    def visitPrograma(self, ctx):
        if ctx.decls() is not None:
            self.visit(ctx.decls())
        self.visit(ctx.cmdComp())
        return self.tabela_simbolos

    def visitDeclTip(self, ctx):
        tipo = ctx.tip().getText().upper()

        for token_id in ctx.listId().ID():
            nome = normalizar_identificador(token_id.getText())
            entrada = self.tabela_simbolos.declarar(nome, tipo)
            if entrada is None:
                self._erro(token_id.symbol, f"identificador '{nome}' ja declarado.")

    def visitCmdComp(self, ctx):
        abre_escopo = self._nivel_cmd_comp > 0
        self._nivel_cmd_comp += 1

        if abre_escopo:
            self.tabela_simbolos.abrir_escopo()

        self.visit(ctx.listCmd())

        if abre_escopo:
            self.tabela_simbolos.fechar_escopo()

        self._nivel_cmd_comp -= 1

    def visitCmdIf(self, ctx):
        tipo_condicao = self.visit(ctx.expr())
        if tipo_condicao != TIPO_BOOLEAN:
            self._erro(ctx.IF().symbol, "condicao do IF deve ser BOOLEAN.")

        for comando in ctx.cmd():
            self.visit(comando)

    def visitCmdWhile(self, ctx):
        tipo_condicao = self.visit(ctx.expr())
        if tipo_condicao != TIPO_BOOLEAN:
            self._erro(ctx.WHILE().symbol, "condicao do WHILE deve ser BOOLEAN.")
        self.visit(ctx.cmd())

    def visitCmdRead(self, ctx):
        for token_id in ctx.listId().ID():
            self._entrada_identificador(token_id)

    def visitCmdWrite(self, ctx):
        self.visit(ctx.listW())

    def visitElemW(self, ctx):
        if ctx.CADEIA() is not None:
            return TIPO_STRING
        return self.visit(ctx.expr())

    def visitCmdAtrib(self, ctx):
        entrada = self._entrada_identificador(ctx.ID())
        tipo_expr = self.visit(ctx.expr())

        if entrada.tipo != tipo_expr:
            self._erro(
                ctx.ID().symbol,
                f"atribuicao incompativel para '{entrada.nome}': esperado {entrada.tipo}, encontrado {tipo_expr}.",
            )

    def visitExpr(self, ctx):
        return self.visit(ctx.logicExpr())

    def visitLogicExpr(self, ctx):
        expressoes = ctx.relationalExpr()
        tipo = self.visit(expressoes[0])

        for indice, operador in enumerate(ctx.OPLOG()):
            tipo_direita = self.visit(expressoes[indice + 1])
            if tipo != TIPO_BOOLEAN or tipo_direita != TIPO_BOOLEAN:
                self._erro(operador.symbol, "operadores logicos exigem operandos BOOLEAN.")
            tipo = TIPO_BOOLEAN

        return tipo

    def visitRelationalExpr(self, ctx):
        expressoes = ctx.additiveExpr()
        tipo_esquerda = self.visit(expressoes[0])

        if ctx.OPREL() is None:
            return tipo_esquerda

        operador = ctx.OPREL()
        tipo_direita = self.visit(expressoes[1])

        if tipo_esquerda != tipo_direita:
            self._erro(operador.symbol, "operadores relacionais exigem operandos do mesmo tipo.")

        return TIPO_BOOLEAN

    def visitAdditiveExpr(self, ctx):
        expressoes = ctx.multiplicativeExpr()
        tipo = self.visit(expressoes[0])

        for indice, operador in enumerate(ctx.OPAD()):
            tipo_direita = self.visit(expressoes[indice + 1])
            if tipo != TIPO_INTEGER or tipo_direita != TIPO_INTEGER:
                self._erro(operador.symbol, "operadores aditivos exigem operandos INTEGER.")
            tipo = TIPO_INTEGER

        return tipo

    def visitMultiplicativeExpr(self, ctx):
        expressoes = ctx.unaryExpr()
        tipo = self.visit(expressoes[0])

        for indice, operador in enumerate(ctx.OPMULT()):
            tipo_direita = self.visit(expressoes[indice + 1])
            if tipo != TIPO_INTEGER or tipo_direita != TIPO_INTEGER:
                self._erro(operador.symbol, "operadores multiplicativos exigem operandos INTEGER.")
            tipo = TIPO_INTEGER

        return tipo

    def visitUnaryExpr(self, ctx):
        if ctx.primaryExpr() is not None:
            return self.visit(ctx.primaryExpr())

        if ctx.OPAD() is not None and ctx.OPAD().getText() == "-":
            valor_negativo = self._valor_literal_negativo(ctx.unaryExpr())
            if valor_negativo is not None:
                self._validar_intervalo_inteiro(valor_negativo, ctx.OPAD().symbol)
                return TIPO_INTEGER

        tipo = self.visit(ctx.unaryExpr())

        if ctx.OPNEG() is not None:
            if tipo != TIPO_BOOLEAN:
                self._erro(ctx.OPNEG().symbol, "operador '~' exige operando BOOLEAN.")
            return TIPO_BOOLEAN

        if tipo != TIPO_INTEGER:
            self._erro(ctx.OPAD().symbol, "operador unario '+' ou '-' exige operando INTEGER.")
        return TIPO_INTEGER

    def visitPrimaryExpr(self, ctx):
        if ctx.ID() is not None:
            return self._entrada_identificador(ctx.ID()).tipo
        if ctx.CTE() is not None:
            valor = int(ctx.CTE().getText())
            self._validar_intervalo_inteiro(valor, ctx.CTE().symbol)
            return TIPO_INTEGER
        if ctx.TRUE() is not None or ctx.FALSE() is not None:
            return TIPO_BOOLEAN
        return self.visit(ctx.expr())

    def _entrada_identificador(self, token_id):
        nome = normalizar_identificador(token_id.getText())
        entrada = self.tabela_simbolos.buscar(nome)
        if entrada is None:
            self._erro(token_id.symbol, f"identificador '{nome}' nao declarado.")
        return entrada

    def _valor_literal_negativo(self, ctx) -> Optional[int]:
        if ctx.primaryExpr() is None:
            return None
        primario = ctx.primaryExpr()
        if primario.CTE() is None:
            return None
        return -int(primario.CTE().getText())

    def _validar_intervalo_inteiro(self, valor, token):
        if valor < MIN_INTEGER or valor > MAX_INTEGER:
            self._erro(token, f"overflow de constante inteira: {valor} fora do intervalo de 2 bytes com sinal.")

    def _erro(self, token, mensagem):
        raise CompilerError(f"Erro semantico na linha {token.line}, coluna {token.column}: {mensagem}")
