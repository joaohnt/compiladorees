from collections import OrderedDict
from dataclasses import dataclass, replace
from typing import Optional

from compiler.semantic import TIPO_BOOLEAN, TIPO_INTEGER, TIPO_STRING, normalizar_identificador
from generated.CompiladorVisitor import CompiladorVisitor


DIRETIVAS_DADOS = {
    TIPO_INTEGER: "dw 0",
    TIPO_BOOLEAN: "db 0",
    TIPO_STRING: "db 256 dup(0)",
}

OPERADORES_ASSEMBLY = {
    "+": "add",
    "-": "sub",
    "*": "imul",
    "<<": "shl",
}

SALTOS_RELACIONAIS = {
    "<": "setl",
    "<=": "setle",
    ">": "setg",
    ">=": "setge",
    "==": "sete",
    "<>": "setne",
}


@dataclass(frozen=True)
class Operando:
    valor: str
    tipo: str
    literal: bool = False


@dataclass(frozen=True)
class Instrucao3AC:
    tipo: str
    resultado: Optional[str] = None
    operador: Optional[str] = None
    arg1: Optional[Operando] = None
    arg2: Optional[Operando] = None
    alvo: Optional[str] = None


class GeradorCodigo(CompiladorVisitor):
    def __init__(self, tabela_simbolos):
        self.tabela_simbolos = tabela_simbolos
        self.instrucoes_3ac = []
        self.instrucoes_3ac_otimizadas = []
        self.temporarios = OrderedDict()
        self.literais = OrderedDict()
        self._proximo_temporario = 0
        self._proximo_rotulo = 0

    def gerar(self, arvore):
        self._coletar_literais(arvore)
        self.visit(arvore)
        self.instrucoes_3ac_otimizadas = Otimizador3AC().otimizar(self.instrucoes_3ac)
        return MontadorAssembly(
            self.tabela_simbolos,
            self.temporarios,
            self.literais,
            self.instrucoes_3ac_otimizadas,
        ).montar()

    def visitPrograma(self, ctx):
        self.visit(ctx.cmdComp())

    def visitCmdComp(self, ctx):
        self.visit(ctx.listCmd())

    def visitListCmd(self, ctx):
        for comando in ctx.cmd():
            self.visit(comando)

    def visitCmd(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitCmdIf(self, ctx):
        rotulo_senao = self._novo_rotulo("ELSE")
        rotulo_fim = self._novo_rotulo("END")
        comandos = ctx.cmd()

        condicao = self.visit(ctx.expr())
        self._emitir(Instrucao3AC("if_false", arg1=condicao, alvo=rotulo_senao))
        self.visit(comandos[0])

        if ctx.ELSE() is not None:
            self._emitir(Instrucao3AC("goto", alvo=rotulo_fim))
            self._emitir(Instrucao3AC("label", alvo=rotulo_senao))
            self.visit(comandos[1])
            self._emitir(Instrucao3AC("label", alvo=rotulo_fim))
        else:
            self._emitir(Instrucao3AC("label", alvo=rotulo_senao))

    def visitCmdWhile(self, ctx):
        rotulo_inicio = self._novo_rotulo("WHILE_START")
        rotulo_fim = self._novo_rotulo("WHILE_END")

        self._emitir(Instrucao3AC("label", alvo=rotulo_inicio))
        condicao = self.visit(ctx.expr())
        self._emitir(Instrucao3AC("if_false", arg1=condicao, alvo=rotulo_fim))
        self.visit(ctx.cmd())
        self._emitir(Instrucao3AC("goto", alvo=rotulo_inicio))
        self._emitir(Instrucao3AC("label", alvo=rotulo_fim))

    def visitCmdRead(self, ctx):
        for token_id in ctx.listId().ID():
            nome = normalizar_identificador(token_id.getText())
            self._emitir(Instrucao3AC("read", resultado=nome))

    def visitCmdWrite(self, ctx):
        self.visit(ctx.listW())

    def visitListW(self, ctx):
        for elemento in ctx.elemW():
            self.visit(elemento)

    def visitElemW(self, ctx):
        if ctx.CADEIA() is not None:
            rotulo = self.literais[ctx.CADEIA().getText()]
            self._emitir(Instrucao3AC("write_str", resultado=rotulo))
            return None

        valor = self.visit(ctx.expr())
        self._emitir(Instrucao3AC("write", arg1=valor))
        return None

    def visitCmdAtrib(self, ctx):
        nome = normalizar_identificador(ctx.ID().getText())
        valor = self.visit(ctx.expr())
        self._emitir(Instrucao3AC("assign", resultado=nome, arg1=valor))

    def visitExpr(self, ctx):
        return self.visit(ctx.logicExpr())

    def visitLogicExpr(self, ctx):
        expressoes = ctx.relationalExpr()
        resultado = self.visit(expressoes[0])

        for indice, operador in enumerate(ctx.OPLOG()):
            direita = self.visit(expressoes[indice + 1])
            temporario = self._novo_temporario(TIPO_BOOLEAN)
            self._emitir(
                Instrucao3AC(
                    "logic",
                    resultado=temporario,
                    operador=operador.getText().upper(),
                    arg1=resultado,
                    arg2=direita,
                )
            )
            resultado = Operando(temporario, TIPO_BOOLEAN)

        return resultado

    def visitRelationalExpr(self, ctx):
        expressoes = ctx.additiveExpr()
        esquerda = self.visit(expressoes[0])

        if ctx.OPREL() is None:
            return esquerda

        direita = self.visit(expressoes[1])
        temporario = self._novo_temporario(TIPO_BOOLEAN)
        self._emitir(
            Instrucao3AC(
                "rel",
                resultado=temporario,
                operador=ctx.OPREL().getText(),
                arg1=esquerda,
                arg2=direita,
            )
        )
        return Operando(temporario, TIPO_BOOLEAN)

    def visitAdditiveExpr(self, ctx):
        expressoes = ctx.multiplicativeExpr()
        resultado = self.visit(expressoes[0])

        for indice, operador in enumerate(ctx.OPAD()):
            direita = self.visit(expressoes[indice + 1])
            temporario = self._novo_temporario(TIPO_INTEGER)
            self._emitir(
                Instrucao3AC(
                    "bin",
                    resultado=temporario,
                    operador=operador.getText(),
                    arg1=resultado,
                    arg2=direita,
                )
            )
            resultado = Operando(temporario, TIPO_INTEGER)

        return resultado

    def visitMultiplicativeExpr(self, ctx):
        expressoes = ctx.unaryExpr()
        resultado = self.visit(expressoes[0])

        for indice, operador in enumerate(ctx.OPMULT()):
            direita = self.visit(expressoes[indice + 1])
            temporario = self._novo_temporario(TIPO_INTEGER)
            self._emitir(
                Instrucao3AC(
                    "bin",
                    resultado=temporario,
                    operador=operador.getText(),
                    arg1=resultado,
                    arg2=direita,
                )
            )
            resultado = Operando(temporario, TIPO_INTEGER)

        return resultado

    def visitUnaryExpr(self, ctx):
        if ctx.primaryExpr() is not None:
            return self.visit(ctx.primaryExpr())

        valor = self.visit(ctx.unaryExpr())

        if ctx.OPNEG() is not None:
            temporario = self._novo_temporario(TIPO_BOOLEAN)
            self._emitir(Instrucao3AC("unary", resultado=temporario, operador="NOT", arg1=valor))
            return Operando(temporario, TIPO_BOOLEAN)

        if ctx.OPAD().getText() == "+":
            return valor

        if valor.literal:
            return Operando(str(-int(valor.valor)), TIPO_INTEGER, True)

        temporario = self._novo_temporario(TIPO_INTEGER)
        self._emitir(Instrucao3AC("unary", resultado=temporario, operador="NEG", arg1=valor))
        return Operando(temporario, TIPO_INTEGER)

    def visitPrimaryExpr(self, ctx):
        if ctx.ID() is not None:
            nome = normalizar_identificador(ctx.ID().getText())
            return Operando(nome, self._tipo_variavel(nome))
        if ctx.CTE() is not None:
            return Operando(ctx.CTE().getText(), TIPO_INTEGER, True)
        if ctx.TRUE() is not None:
            return Operando("1", TIPO_BOOLEAN, True)
        if ctx.FALSE() is not None:
            return Operando("0", TIPO_BOOLEAN, True)
        return self.visit(ctx.expr())

    def _coletar_literais(self, contexto):
        if hasattr(contexto, "CADEIA") and contexto.CADEIA() is not None:
            texto = contexto.CADEIA().getText()
            if texto not in self.literais:
                self.literais[texto] = f"_str_{len(self.literais)}"

        for filho in getattr(contexto, "children", []) or []:
            self._coletar_literais(filho)

    def _tipo_variavel(self, nome):
        entrada = self.tabela_simbolos.buscar(nome)
        if entrada is None:
            return self.temporarios[nome]
        return entrada.tipo

    def _novo_temporario(self, tipo):
        nome = f"t_{self._proximo_temporario}"
        self._proximo_temporario += 1
        self.temporarios[nome] = tipo
        return nome

    def _novo_rotulo(self, prefixo):
        rotulo = f"L_{prefixo}_{self._proximo_rotulo}"
        self._proximo_rotulo += 1
        return rotulo

    def _emitir(self, instrucao):
        self.instrucoes_3ac.append(instrucao)


class Otimizador3AC:
    def otimizar(self, instrucoes):
        constantes = {}
        resultado = []

        for instrucao in instrucoes:
            if instrucao.tipo == "label":
                constantes.clear()
                resultado.append(instrucao)
                continue

            if instrucao.tipo == "goto":
                constantes.clear()
                resultado.append(instrucao)
                continue

            if instrucao.tipo == "read":
                constantes.pop(instrucao.resultado, None)
                resultado.append(instrucao)
                continue

            instrucao = self._substituir_constantes(instrucao, constantes)
            dobrada = self._dobrar_constante(instrucao)

            if dobrada is not None:
                instrucao = dobrada

            instrucao = self._reduzir_forca(instrucao)

            if instrucao.tipo == "assign":
                if instrucao.arg1.literal:
                    constantes[instrucao.resultado] = instrucao.arg1
                else:
                    constantes.pop(instrucao.resultado, None)
                resultado.append(instrucao)
                continue

            if instrucao.tipo == "if_false" and instrucao.arg1.literal:
                if int(instrucao.arg1.valor) == 0:
                    constantes.clear()
                    resultado.append(Instrucao3AC("goto", alvo=instrucao.alvo))
                continue

            if instrucao.resultado is not None:
                constantes.pop(instrucao.resultado, None)

            resultado.append(instrucao)

        return resultado

    def _substituir_constantes(self, instrucao, constantes):
        arg1 = self._resolver_constante(instrucao.arg1, constantes)
        arg2 = self._resolver_constante(instrucao.arg2, constantes)
        return replace(instrucao, arg1=arg1, arg2=arg2)

    def _resolver_constante(self, operando, constantes):
        if operando is None or operando.literal:
            return operando
        return constantes.get(operando.valor, operando)

    def _dobrar_constante(self, instrucao):
        if instrucao.tipo == "unary" and instrucao.arg1.literal:
            valor = int(instrucao.arg1.valor)
            if instrucao.operador == "NEG":
                return Instrucao3AC(
                    "assign",
                    resultado=instrucao.resultado,
                    arg1=Operando(str(-valor), TIPO_INTEGER, True),
                )
            if instrucao.operador == "NOT":
                return Instrucao3AC(
                    "assign",
                    resultado=instrucao.resultado,
                    arg1=Operando("0" if valor else "1", TIPO_BOOLEAN, True),
                )

        if instrucao.arg1 is None or instrucao.arg2 is None:
            return None
        if not instrucao.arg1.literal or not instrucao.arg2.literal:
            return None

        esquerda = int(instrucao.arg1.valor)
        direita = int(instrucao.arg2.valor)

        if instrucao.tipo == "bin":
            valor = self._calcular_binario(instrucao.operador, esquerda, direita)
            if valor is None:
                return None
            return Instrucao3AC(
                "assign",
                resultado=instrucao.resultado,
                arg1=Operando(str(valor), TIPO_INTEGER, True),
            )

        if instrucao.tipo == "rel":
            valor = self._calcular_relacional(instrucao.operador, esquerda, direita)
            return Instrucao3AC(
                "assign",
                resultado=instrucao.resultado,
                arg1=Operando("1" if valor else "0", TIPO_BOOLEAN, True),
            )

        if instrucao.tipo == "logic":
            if instrucao.operador == "AND":
                valor = esquerda and direita
            else:
                valor = esquerda or direita
            return Instrucao3AC(
                "assign",
                resultado=instrucao.resultado,
                arg1=Operando("1" if valor else "0", TIPO_BOOLEAN, True),
            )

        return None

    def _calcular_binario(self, operador, esquerda, direita):
        if operador == "+":
            return esquerda + direita
        if operador == "-":
            return esquerda - direita
        if operador == "*":
            return esquerda * direita
        if operador == "/" and direita != 0:
            return esquerda // direita
        return None

    def _calcular_relacional(self, operador, esquerda, direita):
        if operador == "<":
            return esquerda < direita
        if operador == "<=":
            return esquerda <= direita
        if operador == ">":
            return esquerda > direita
        if operador == ">=":
            return esquerda >= direita
        if operador == "==":
            return esquerda == direita
        return esquerda != direita

    def _reduzir_forca(self, instrucao):
        if instrucao.tipo != "bin" or instrucao.operador != "*":
            return instrucao

        if instrucao.arg2.literal and self._potencia_de_dois(int(instrucao.arg2.valor)):
            expoente = self._expoente_potencia_de_dois(int(instrucao.arg2.valor))
            return replace(instrucao, operador="<<", arg2=Operando(str(expoente), TIPO_INTEGER, True))

        if instrucao.arg1.literal and self._potencia_de_dois(int(instrucao.arg1.valor)):
            expoente = self._expoente_potencia_de_dois(int(instrucao.arg1.valor))
            return replace(
                instrucao,
                operador="<<",
                arg1=instrucao.arg2,
                arg2=Operando(str(expoente), TIPO_INTEGER, True),
            )

        return instrucao

    def _potencia_de_dois(self, valor):
        return valor > 0 and valor & (valor - 1) == 0

    def _expoente_potencia_de_dois(self, valor):
        expoente = 0
        while valor > 1:
            valor //= 2
            expoente += 1
        return expoente


class MontadorAssembly:
    def __init__(self, tabela_simbolos, temporarios, literais, instrucoes):
        self.tabela_simbolos = tabela_simbolos
        self.temporarios = temporarios
        self.literais = literais
        self.instrucoes = instrucoes
        self.linhas = []
        self.tipos = {entrada.nome: entrada.tipo for entrada in tabela_simbolos.entradas()}
        self.tipos.update(temporarios)

    def montar(self):
        self._emitir(".data")
        for entrada in self.tabela_simbolos.entradas():
            self._emitir(f"{entrada.nome} {DIRETIVAS_DADOS[entrada.tipo]}")
        for nome, tipo in self.temporarios.items():
            self._emitir(f"{nome} {DIRETIVAS_DADOS[tipo]}")
        for texto, rotulo in self.literais.items():
            self._emitir(f"{rotulo} db {texto}, 0")

        self._emitir("")
        self._emitir(".code")
        self._emitir("START:")

        for instrucao in self.instrucoes:
            self._montar_instrucao(instrucao)

        self._emitir("    hlt")
        self._emitir("END START")
        return "\n".join(self.linhas)

    def _montar_instrucao(self, instrucao):
        if instrucao.tipo == "label":
            self._emitir(f"{instrucao.alvo}:")
        elif instrucao.tipo == "goto":
            self._emitir(f"    jmp {instrucao.alvo}")
        elif instrucao.tipo == "if_false":
            self._montar_if_false(instrucao)
        elif instrucao.tipo == "assign":
            self._montar_atribuicao(instrucao)
        elif instrucao.tipo == "bin":
            self._montar_binaria(instrucao)
        elif instrucao.tipo == "rel":
            self._montar_relacional(instrucao)
        elif instrucao.tipo == "logic":
            self._montar_logica(instrucao)
        elif instrucao.tipo == "unary":
            self._montar_unaria(instrucao)
        elif instrucao.tipo == "read":
            self._montar_read(instrucao)
        elif instrucao.tipo == "write":
            self._montar_write(instrucao)
        elif instrucao.tipo == "write_str":
            self._emitir(f"    push offset {instrucao.resultado}")
            self._emitir("    call _print_string")

    def _montar_atribuicao(self, instrucao):
        tipo_destino = self._tipo_nome(instrucao.resultado)
        destino = self._memoria(instrucao.resultado)

        if tipo_destino == TIPO_INTEGER:
            if instrucao.arg1.literal:
                self._emitir(f"    mov {destino}, {instrucao.arg1.valor}")
            else:
                self._emitir(f"    mov ax, {self._valor(instrucao.arg1)}")
                self._emitir(f"    mov {destino}, ax")
            return

        if tipo_destino == TIPO_BOOLEAN:
            if instrucao.arg1.literal:
                self._emitir(f"    mov {destino}, {instrucao.arg1.valor}")
            else:
                self._emitir(f"    mov al, {self._valor(instrucao.arg1)}")
                self._emitir(f"    mov {destino}, al")
            return

        self._emitir(f"    ; atribuicao de STRING para {instrucao.resultado} nao requer copia neste gerador")

    def _montar_binaria(self, instrucao):
        self._emitir(f"    mov ax, {self._valor(instrucao.arg1)}")

        if instrucao.operador == "/":
            self._emitir("    cwd")
            if instrucao.arg2.literal:
                self._emitir(f"    mov bx, {instrucao.arg2.valor}")
                self._emitir("    idiv bx")
            else:
                self._emitir(f"    idiv {self._valor(instrucao.arg2)}")
        elif instrucao.operador == "*":
            self._emitir(f"    imul ax, {self._valor(instrucao.arg2)}")
        elif instrucao.operador == "<<":
            self._emitir(f"    shl ax, {instrucao.arg2.valor}")
        else:
            self._emitir(f"    {OPERADORES_ASSEMBLY[instrucao.operador]} ax, {self._valor(instrucao.arg2)}")

        self._emitir(f"    mov {self._memoria(instrucao.resultado)}, ax")

    def _montar_relacional(self, instrucao):
        registrador = "ax" if instrucao.arg1.tipo == TIPO_INTEGER else "al"
        self._emitir(f"    mov {registrador}, {self._valor(instrucao.arg1)}")
        self._emitir(f"    cmp {registrador}, {self._valor(instrucao.arg2)}")
        self._emitir(f"    {SALTOS_RELACIONAIS[instrucao.operador]} al")
        self._emitir(f"    mov {self._memoria(instrucao.resultado)}, al")

    def _montar_logica(self, instrucao):
        operador = "and" if instrucao.operador == "AND" else "or"
        self._emitir(f"    mov al, {self._valor(instrucao.arg1)}")
        self._emitir(f"    {operador} al, {self._valor(instrucao.arg2)}")
        self._emitir(f"    mov {self._memoria(instrucao.resultado)}, al")

    def _montar_unaria(self, instrucao):
        if instrucao.operador == "NEG":
            self._emitir(f"    mov ax, {self._valor(instrucao.arg1)}")
            self._emitir("    neg ax")
            self._emitir(f"    mov {self._memoria(instrucao.resultado)}, ax")
            return

        self._emitir(f"    mov al, {self._valor(instrucao.arg1)}")
        self._emitir("    xor al, 1")
        self._emitir(f"    mov {self._memoria(instrucao.resultado)}, al")

    def _montar_if_false(self, instrucao):
        if instrucao.arg1.literal:
            self._emitir(f"    mov al, {instrucao.arg1.valor}")
        else:
            self._emitir(f"    mov al, {self._valor(instrucao.arg1)}")
        self._emitir("    cmp al, 0")
        self._emitir(f"    je {instrucao.alvo}")

    def _montar_read(self, instrucao):
        tipo = self._tipo_nome(instrucao.resultado)
        if tipo == TIPO_INTEGER:
            self._emitir("    call _read_integer")
            self._emitir(f"    mov {self._memoria(instrucao.resultado)}, ax")
        elif tipo == TIPO_BOOLEAN:
            self._emitir("    call _read_boolean")
            self._emitir(f"    mov {self._memoria(instrucao.resultado)}, al")
        else:
            self._emitir(f"    push offset {instrucao.resultado}")
            self._emitir("    call _read_string")

    def _montar_write(self, instrucao):
        if instrucao.arg1.tipo == TIPO_INTEGER:
            if instrucao.arg1.literal:
                self._emitir(f"    push {instrucao.arg1.valor}")
            else:
                self._emitir(f"    push {self._valor(instrucao.arg1)}")
            self._emitir("    call _print_integer")
        elif instrucao.arg1.tipo == TIPO_BOOLEAN:
            if instrucao.arg1.literal:
                self._emitir(f"    mov ax, {instrucao.arg1.valor}")
            else:
                self._emitir(f"    mov al, {self._valor(instrucao.arg1)}")
                self._emitir("    movzx ax, al")
            self._emitir("    push ax")
            self._emitir("    call _print_boolean")
        else:
            self._emitir(f"    push offset {instrucao.arg1.valor}")
            self._emitir("    call _print_string")

    def _valor(self, operando):
        if operando.literal:
            return operando.valor
        return self._memoria(operando.valor)

    def _memoria(self, nome):
        tipo = self._tipo_nome(nome)
        if tipo == TIPO_BOOLEAN:
            return f"byte ptr [{nome}]"
        return f"word ptr [{nome}]"

    def _tipo_nome(self, nome):
        return self.tipos[nome]

    def _emitir(self, linha):
        self.linhas.append(linha)
