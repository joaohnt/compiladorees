# Relatorio - Construcao de um Compilador

## Identificacao

Disciplina: Linguagens Formais e Compiladores

Projeto: analisador lexico, analisador sintatico, analisador semantico e gerador de codigo para a linguagem proposta.

## Visao geral

O compilador foi implementado em Python com ANTLR4. A gramatica fica em `grammar/Compilador.g4` e os arquivos gerados pelo ANTLR estao versionados em `src/generated/`.

O fluxo de compilacao e:

1. leitura do arquivo fonte;
2. validacao lexica;
3. analise sintatica;
4. validacoes adicionais de comandos compostos;
5. analise semantica;
6. geracao de codigo final em formato textual com secoes `.data` e `.code`.

## Analise lexica

A gramatica reconhece palavras reservadas, identificadores, constantes inteiras, cadeias, operadores, delimitadores e comentarios de linha. As palavras reservadas sao reconhecidas sem diferenciar letras maiusculas de minusculas.

As validacoes lexicas adicionais estao em `src/main.py`:

- identificador com mais de 16 caracteres gera aviso e passa a ser tratado apenas pelos 16 primeiros caracteres;
- cadeia de caracteres fechada na mesma linha;
- rejeicao de simbolos invalidos.

## Analise sintatica

A analise sintatica e feita pelo parser gerado a partir de `grammar/Compilador.g4`. A linguagem aceita:

- declaracoes de variaveis dos tipos `INTEGER`, `BOOLEAN` e `STRING`;
- comandos compostos com `BEGIN` e `END`;
- atribuicao;
- leitura com `READ`;
- escrita com `WRITE`;
- condicional `IF ... THEN ... ELSE`;
- repeticao `WHILE ... DO`;
- expressoes aritmeticas, relacionais e logicas.

O compilador tambem rejeita bloco vazio e ponto e virgula extra antes de `END`.

## Analise semantica

A analise semantica foi implementada em `src/compiler/semantic.py`, na classe `AnalisadorSemantico`.

Durante a visita a arvore sintatica, o analisador monta uma tabela de simbolos com escopos encadeados. Cada entrada guarda o lexema ja truncado, o tipo estatico, o deslocamento em bytes e o nivel de escopo.

Regras verificadas:

- identificador nao pode ser declarado mais de uma vez;
- identificador precisa ser declarado antes de ser usado;
- constantes inteiras precisam estar no intervalo assinado de 2 bytes, de `-32768` ate `32767`;
- atribuicao exige compatibilidade entre o tipo da variavel e o tipo da expressao;
- `IF` e `WHILE` exigem condicao `BOOLEAN`;
- operadores `+`, `-`, `*` e `/` exigem operandos `INTEGER`;
- operadores relacionais exigem operandos do mesmo tipo e retornam `BOOLEAN`;
- operadores `AND`, `OR` e `~` exigem operandos `BOOLEAN`.

## Geracao de codigo

A geracao de codigo foi implementada em `src/compiler/codegen.py`, na classe `GeradorCodigo`.

A arvore sintatica validada e traduzida primeiro para codigo intermediario em tres enderecos (3AC). Esse formato usa temporarios (`t_0`, `t_1`, ...) e rotulos (`L_ELSE_0`, `L_WHILE_START_0`, ...) para linearizar expressoes, condicionais e repeticoes.

Antes da montagem final, o gerador aplica otimizacoes simples:

- dobramento de constantes;
- propagacao de constantes em trechos lineares;
- remocao de desvios condicionais constantes;
- reducao de forca em multiplicacoes por potencia de dois, convertendo para `shl`.

Depois disso, o 3AC otimizado e traduzido para Assembly x86 em sintaxe Intel, com registradores de 16 bits para inteiros (`ax`, `bx`) e registradores baixos para booleanos (`al`).

Na secao `.data`, todas as variaveis da tabela de simbolos sao alocadas:

- variaveis `INTEGER` usam a diretiva `dw 0`;
- variaveis `BOOLEAN` usam a diretiva `db 0`;
- variaveis `STRING` usam a diretiva `db 256 dup(0)`;
- temporarios do 3AC tambem sao reservados com `dw` ou `db`, conforme o tipo inferido;
- literais de texto usados em `WRITE` recebem rotulos auxiliares, como `_str_0 db "texto", 0`.

Padroes principais da traducao final:

- atribuicoes inteiras usam `mov word ptr [nome], valor`;
- atribuicoes booleanas usam `mov byte ptr [nome], valor`;
- operacoes aritmeticas usam `mov`, `add`, `sub`, `imul`, `idiv` e `shl`;
- comparacoes usam `cmp` seguido de `setl`, `setle`, `setg`, `setge`, `sete` ou `setne`;
- condicionais e repeticoes usam rotulos, `je` e `jmp`;
- `WRITE` inteiro usa `push word ptr [nome]` e `call _print_integer`;
- `WRITE` de cadeia usa `push offset _str_n` e `call _print_string`;
- `hlt`: fim da execucao.

## Testes

Os testes ficam em `tests/test_lexer_parser.py` e cobrem:

- erros lexicos;
- erros sintaticos;
- erros semanticos;
- geracao de codigo com secoes `.data` e `.code` para programa valido.

Com as dependencias instaladas, os testes podem ser executados com:

```bash
python -m unittest discover -s tests -v
```

## Exemplos

Arquivos de exemplo:

- `examples/programa_ok.txt`: programa valido da primeira etapa;
- `examples/programa_codigo.txt`: programa valido com geracao de codigo;
- `examples/programa_codigo.asm`: saida final gerada a partir de `programa_codigo.txt`;
- `examples/erro_lexico.txt`: exemplo de erro lexico;
- `examples/erro_sintatico.txt`: exemplo de erro sintatico;
- `examples/erro_semantico.txt`: exemplo de erro semantico.
