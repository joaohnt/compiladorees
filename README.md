# Compilador Simples com ANTLR4 e Python

Projeto de um compilador simples para a linguagem proposta na disciplina de Linguagens Formais e Compiladores.

## Estrutura

- `grammar/Compilador.g4`: gramática usada pelo ANTLR4.
- `src/main.py`: ponto de entrada do compilador.
- `src/compiler/`: erros compartilhados pelo analisador.
- `src/generated/`: lexer, parser, listener e visitor gerados pelo ANTLR4.
- `examples/`: programas de exemplo.
- `tests/`: testes automatizados.

## Instalação

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Como executar

```powershell
python .\src\main.py .\examples\programa_ok.txt
```

Também é possível usar o arquivo em lote:

```powershell
.\executar_compilador.bat .\examples\programa_ok.txt
```

## Como gerar o parser

Os arquivos gerados já estão versionados em `src/generated/`. Caso a gramática seja alterada, baixe o ANTLR4 e execute:

```powershell
$env:ANTLR_JAR = "C:\caminho\para\antlr-4.13.2-complete.jar"
.\gerar_parser.bat
```

## Saída

Ao executar, o compilador:

1. imprime os tokens reconhecidos;
2. valida a sintaxe;
3. exibe a árvore sintática gerada pelo ANTLR.
