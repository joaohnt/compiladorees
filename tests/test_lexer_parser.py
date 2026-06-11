from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
import io
import sys
import unittest


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from main import compilar_arquivo


class LexerParserTests(unittest.TestCase):
    def compilar(self, fonte):
        with TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "programa.txt"
            caminho.write_text(fonte, encoding="utf-8")
            with redirect_stdout(io.StringIO()):
                return compilar_arquivo(caminho)

    def saida_compilacao(self, fonte):
        with TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "programa.txt"
            caminho.write_text(fonte, encoding="utf-8")
            buffer = io.StringIO()
            with redirect_stdout(buffer):
                codigo = compilar_arquivo(caminho)
            return codigo, buffer.getvalue()

    def assert_falha(self, fonte, trecho):
        with self.assertRaises(Exception) as erro:
            self.compilar(fonte)
        self.assertIn(trecho, str(erro.exception))

    def test_erros_lexicos(self):
        casos = [
            ("PROGRAM teste; BEGIN WRITE(@) END.", "simbolo invalido '@'"),
            ('PROGRAM teste; BEGIN WRITE("texto) END.', "cadeia nao fechada"),
            ('PROGRAM teste; BEGIN WRITE("texto\n") END.', "cadeia nao fechada"),
        ]
        for fonte, trecho in casos:
            with self.subTest(trecho=trecho):
                self.assert_falha(fonte, trecho)

    def test_erros_sintaticos(self):
        casos = [
            ("teste; BEGIN WRITE(1) END.", "Erro sintatico"),
            ("PROGRAM teste BEGIN WRITE(1) END.", "Erro sintatico"),
            ("PROGRAM teste; VAR x INTEGER; BEGIN WRITE(1) END.", "Erro sintatico"),
            ("PROGRAM teste; VAR x : INTEGER BEGIN WRITE(1) END.", "Erro sintatico"),
            ("PROGRAM teste; VAR x : REAL; BEGIN WRITE(1) END.", "Erro sintatico"),
            ("PROGRAM teste; BEGIN END.", "deve possuir ao menos um comando"),
            ("PROGRAM teste; BEGIN WRITE(1); END.", "ponto e virgula extra"),
            ("PROGRAM teste; BEGIN READ x) END.", "Erro sintatico"),
            ("PROGRAM teste; BEGIN READ(x END.", "Erro sintatico"),
            ("PROGRAM teste; BEGIN WRITE(1 END.", "Erro sintatico"),
            ("PROGRAM teste; BEGIN x = 1 END.", "Erro lexico"),
            ("PROGRAM teste; BEGIN IF TRUE WRITE(1) END.", "Erro sintatico"),
            ("PROGRAM teste; BEGIN WHILE TRUE WRITE(1) END.", "Erro sintatico"),
            ("PROGRAM teste; BEGIN WRITE(1) .", "Erro sintatico"),
            ("PROGRAM teste; BEGIN WRITE(1) END", "Erro sintatico"),
            ("PROGRAM teste; BEGIN WRITE(1,,2) END.", "Erro sintatico"),
        ]
        for fonte, trecho in casos:
            with self.subTest(fonte=fonte):
                self.assert_falha(fonte, trecho)

    def test_erros_semanticos(self):
        casos = [
            (
                "PROGRAM teste; VAR x : INTEGER; x : BOOLEAN; BEGIN WRITE(x) END.",
                "identificador 'x' ja declarado",
            ),
            (
                "PROGRAM teste; VAR x : INTEGER; BEGIN y := 1 END.",
                "identificador 'y' nao declarado",
            ),
            (
                "PROGRAM teste; VAR x : INTEGER; BEGIN x := TRUE END.",
                "atribuicao incompativel",
            ),
            (
                "PROGRAM teste; VAR x : INTEGER; BEGIN IF x THEN WRITE(x) END.",
                "condicao do IF deve ser BOOLEAN",
            ),
            (
                "PROGRAM teste; VAR x : INTEGER; BEGIN WHILE x DO WRITE(x) END.",
                "condicao do WHILE deve ser BOOLEAN",
            ),
            (
                "PROGRAM teste; VAR x : INTEGER; b : BOOLEAN; BEGIN x := b + 1 END.",
                "operadores aditivos exigem operandos INTEGER",
            ),
            (
                "PROGRAM teste; VAR x : INTEGER; b : BOOLEAN; BEGIN b := x AND TRUE END.",
                "operadores logicos exigem operandos BOOLEAN",
            ),
            (
                "PROGRAM teste; VAR x : INTEGER; b : BOOLEAN; BEGIN b := x < TRUE END.",
                "operadores relacionais exigem operandos do mesmo tipo",
            ),
            (
                "PROGRAM teste; BEGIN WRITE(32768) END.",
                "overflow de constante inteira",
            ),
            (
                "PROGRAM teste; BEGIN WRITE(-32769) END.",
                "overflow de constante inteira",
            ),
        ]
        for fonte, trecho in casos:
            with self.subTest(trecho=trecho):
                self.assert_falha(fonte, trecho)

    def test_identificador_longo_e_truncado_com_aviso(self):
        codigo, saida = self.saida_compilacao(
            """
            PROGRAM identificadormuitolongo;
            VAR
                identificadormuitolongo : INTEGER;
            BEGIN
                identificadormuitolongo := 1;
                WRITE(identificadormuitolongo)
            END.
            """
        )

        self.assertIn("Aviso lexico", saida)
        self.assertIn("identificadormui dw 0", codigo)
        self.assertIn("word ptr [identificadormui]", codigo)

    def test_limite_inferior_de_inteiro_com_sinal(self):
        codigo = self.compilar("PROGRAM teste; VAR x : INTEGER; BEGIN x := -32768; WRITE(x) END.")

        self.assertIn("mov word ptr [x], -32768", codigo)

    def test_gera_codigo_com_secao_de_dados_e_codigo(self):
        codigo = self.compilar(
            """
            PROGRAM teste;
            VAR
                x, y : INTEGER;
                ok : BOOLEAN;
            BEGIN
                READ(x);
                y := x * 2 + 1;
                ok := y >= 10;
                IF ok THEN
                    WRITE("sim", y)
                ELSE
                    WRITE("nao")
            END.
            """
        )

        self.assertIn(".data", codigo)
        self.assertIn("x dw 0", codigo)
        self.assertIn("y dw 0", codigo)
        self.assertIn("ok db 0", codigo)
        self.assertIn("t_0 dw 0", codigo)
        self.assertIn("t_1 dw 0", codigo)
        self.assertIn("t_2 db 0", codigo)
        self.assertIn('_str_0 db "sim", 0', codigo)
        self.assertIn(".code", codigo)
        self.assertIn("call _read_integer", codigo)
        self.assertIn("shl ax, 1", codigo)
        self.assertIn("cmp ax, 10", codigo)
        self.assertIn("setge al", codigo)
        self.assertIn("je L_ELSE_", codigo)
        self.assertIn("push offset _str_0", codigo)
        self.assertIn("call _print_integer", codigo)
        self.assertTrue(codigo.endswith("END START"))


if __name__ == "__main__":
    unittest.main()
