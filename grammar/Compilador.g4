grammar Compilador;

options {
    language = Python3;
}

programa
    : PROGRAM ID PVIG decls? cmdComp PONTO EOF
    ;

decls
    : VAR declTip+
    ;

declTip
    : listId DPONTOS tip PVIG
    ;

listId
    : ID (VIG ID)*
    ;

tip
    : INTEGER
    | BOOLEAN
    | STRING
    ;

cmdComp
    : BEGIN listCmd END
    ;

listCmd
    : cmd (PVIG cmd)*
    ;

cmd
    : cmdIf
    | cmdWhile
    | cmdRead
    | cmdWrite
    | cmdAtrib
    | cmdComp
    ;

cmdIf
    : IF expr THEN cmd (ELSE cmd)?
    ;

cmdWhile
    : WHILE expr DO cmd
    ;

cmdRead
    : READ ABPAR listId FPAR
    ;

cmdWrite
    : WRITE ABPAR listW FPAR
    ;

listW
    : elemW (VIG elemW)*
    ;

elemW
    : expr
    | CADEIA
    ;

cmdAtrib
    : ID ATRIB expr
    ;

expr
    : logicExpr
    ;

logicExpr
    : relationalExpr (OPLOG relationalExpr)*
    ;

relationalExpr
    : additiveExpr (OPREL additiveExpr)?
    ;

additiveExpr
    : multiplicativeExpr (OPAD multiplicativeExpr)*
    ;

multiplicativeExpr
    : unaryExpr (OPMULT unaryExpr)*
    ;

unaryExpr
    : OPNEG unaryExpr
    | OPAD unaryExpr
    | primaryExpr
    ;

primaryExpr
    : ID
    | CTE
    | TRUE
    | FALSE
    | ABPAR expr FPAR
    ;

PROGRAM : P R O G R A M;
INTEGER : I N T E G E R;
BOOLEAN : B O O L E A N;
STRING  : S T R I N G;
BEGIN   : B E G I N;
END     : E N D;
WHILE   : W H I L E;
DO      : D O;
READ    : R E A D;
VAR     : V A R;
FALSE   : F A L S E;
TRUE    : T R U E;
WRITE   : W R I T E;
IF      : I F;
THEN    : T H E N;
ELSE    : E L S E;

OPAD
    : '+'
    | '-'
    ;

OPMULT
    : '*'
    | '/'
    ;

OPLOG
    : O R
    | A N D
    ;

OPNEG
    : '~'
    ;

OPREL
    : '<='
    | '>='
    | '=='
    | '<>'
    | '<'
    | '>'
    ;

PVIG    : ';';
PONTO   : '.';
DPONTOS : ':';
VIG     : ',';
ABPAR   : '(';
FPAR    : ')';
ATRIB   : ':=';

CADEIA
    : '"' (~["\r\n])* '"'
    ;

CTE
    : [0-9]+
    ;

ID
    : [a-zA-Z] [a-zA-Z0-9]*
    ;

COMMENT
    : '//' ~[\r\n]* -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

UNCLOSED_STRING
    : '"' (~["\r\n])* ('\r'? '\n' | EOF)
    ;

ERROR_CHAR
    : .
    ;

fragment A : [aA];
fragment B : [bB];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
