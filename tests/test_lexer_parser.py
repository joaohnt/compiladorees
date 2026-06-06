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
                compilar_arquivo(caminho)

    def assert_falha(self, fonte, trecho):
        with self.assertRaises(Exception) as erro:
            self.compilar(fonte)
        self.assertIn(trecho, str(erro.exception))

    def test_erros_lexicos(self):
        casos = [
            ("PROGRAM teste; BEGIN WRITE(@) END.", "simbolo invalido '@'"),
            ('PROGRAM teste; BEGIN WRITE("texto) END.', "cadeia nao fechada"),
            ('PROGRAM teste; BEGIN WRITE("texto\n") END.', "cadeia nao fechada"),
            ("PROGRAM teste; BEGIN WRITE(32769) END.", "constante inteira fora do limite"),
            (
                "PROGRAM identificadormuitolongo; BEGIN WRITE(1) END.",
                "excede o limite de 16 caracteres",
            ),
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


if __name__ == "__main__":
    unittest.main()
