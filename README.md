# Compilador Simples com ANTLR4 e Python

Projeto de um compilador simples para a linguagem proposta na disciplina de Linguagens Formais e Compiladores.

## Estrutura

- `grammar/Compilador.g4`: gramática usada pelo ANTLR4.
- `src/main.py`: ponto de entrada do compilador.
- `src/compiler/`: erros compartilhados, analisador semântico e gerador de código.
- `src/generated/`: lexer, parser, listener e visitor gerados pelo ANTLR4.
- `examples/`: programas de exemplo.
- `examples/programa_codigo.asm`: exemplo de código final gerado.
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

Para salvar o código gerado em um arquivo:

```powershell
python .\src\main.py .\examples\programa_codigo.txt -o .\codigo_gerado.asm
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
3. exibe a árvore sintática gerada pelo ANTLR;
4. valida as regras semânticas;
5. exibe a tabela de símbolos;
6. gera código final em formato textual com seções `.data` e `.code`.

## Parte 2

A segunda etapa adiciona:

- tabela de símbolos com identificador truncado, tipo, deslocamento e escopo;
- erro para identificador duplicado;
- erro para identificador usado sem declaração;
- aviso para identificadores com mais de 16 caracteres, usando apenas os 16 primeiros;
- verificação de constantes inteiras no intervalo assinado de 2 bytes (`-32768` a `32767`);
- verificação de tipo em atribuições;
- verificação de expressões aritméticas, relacionais e lógicas;
- exigência de expressão `BOOLEAN` em `IF` e `WHILE`;
- geração interna de código intermediário em 3 endereços;
- otimizações simples sobre o 3AC;
- geração final em Assembly x86 com seção `.data` e seção `.code`.

Exemplo de saída gerada:

```text
.data
x dw 0
y dw 0
ok db 0
t_0 dw 0
t_1 dw 0
t_2 db 0
_str_0 db "valor aceito", 0

.code
START:
    call _read_integer
    mov word ptr [x], ax
    mov ax, word ptr [x]
    shl ax, 1
    mov word ptr [t_0], ax
    mov ax, word ptr [t_0]
    add ax, 1
    mov word ptr [t_1], ax
    mov ax, word ptr [t_1]
    mov word ptr [y], ax
    hlt
END START
```

Na seção `.data`, variáveis `INTEGER` usam `dw 0`, variáveis `BOOLEAN` usam `db 0`, e variáveis `STRING` usam `db 256 dup(0)`. Temporários gerados no 3AC também são reservados nessa seção. Literais de texto usados em `WRITE` recebem rótulos auxiliares.

Padrões principais na saída final:

- `mov word ptr [x], 5`: grava inteiro de 2 bytes.
- `mov byte ptr [ok], 1`: grava booleano de 1 byte.
- `cmp` seguido de `setl`, `setle`, `setg`, `setge`, `sete` ou `setne`: gera resultado booleano para comparações.
- `je` e `jmp`: desvios para `IF` e `WHILE`.
- `call _read_integer`, `call _print_integer`, `call _print_string`: rotinas externas de entrada e saída.
- `hlt`: fim do programa no arquivo gerado.

## Relatório

O arquivo `RELATORIO.md` descreve a construção do compilador, as classes principais, as regras semânticas implementadas e o formato do código gerado.

## Testes

```powershell
python -m unittest discover -s tests -v
```
