# Generated from grammar/Compilador.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,183,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,1,0,1,0,3,0,49,8,0,1,0,1,0,1,0,1,0,1,1,1,
        1,4,1,57,8,1,11,1,12,1,58,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,69,
        8,3,10,3,12,3,72,9,3,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,5,6,83,
        8,6,10,6,12,6,86,9,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,94,8,7,1,8,1,8,
        1,8,1,8,1,8,1,8,3,8,102,8,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,
        10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,5,12,122,8,12,10,
        12,12,12,125,9,12,1,13,1,13,3,13,129,8,13,1,14,1,14,1,14,1,14,1,
        15,1,15,1,16,1,16,1,16,5,16,140,8,16,10,16,12,16,143,9,16,1,17,1,
        17,1,17,3,17,148,8,17,1,18,1,18,1,18,5,18,153,8,18,10,18,12,18,156,
        9,18,1,19,1,19,1,19,5,19,161,8,19,10,19,12,19,164,9,19,1,20,1,20,
        1,20,1,20,1,20,3,20,171,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,3,21,181,8,21,1,21,0,0,22,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,0,1,1,0,2,4,182,0,44,1,0,0,0,2,54,1,0,
        0,0,4,60,1,0,0,0,6,65,1,0,0,0,8,73,1,0,0,0,10,75,1,0,0,0,12,79,1,
        0,0,0,14,93,1,0,0,0,16,95,1,0,0,0,18,103,1,0,0,0,20,108,1,0,0,0,
        22,113,1,0,0,0,24,118,1,0,0,0,26,128,1,0,0,0,28,130,1,0,0,0,30,134,
        1,0,0,0,32,136,1,0,0,0,34,144,1,0,0,0,36,149,1,0,0,0,38,157,1,0,
        0,0,40,170,1,0,0,0,42,180,1,0,0,0,44,45,5,1,0,0,45,46,5,31,0,0,46,
        48,5,22,0,0,47,49,3,2,1,0,48,47,1,0,0,0,48,49,1,0,0,0,49,50,1,0,
        0,0,50,51,3,10,5,0,51,52,5,23,0,0,52,53,5,0,0,1,53,1,1,0,0,0,54,
        56,5,10,0,0,55,57,3,4,2,0,56,55,1,0,0,0,57,58,1,0,0,0,58,56,1,0,
        0,0,58,59,1,0,0,0,59,3,1,0,0,0,60,61,3,6,3,0,61,62,5,24,0,0,62,63,
        3,8,4,0,63,64,5,22,0,0,64,5,1,0,0,0,65,70,5,31,0,0,66,67,5,25,0,
        0,67,69,5,31,0,0,68,66,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,
        1,0,0,0,71,7,1,0,0,0,72,70,1,0,0,0,73,74,7,0,0,0,74,9,1,0,0,0,75,
        76,5,5,0,0,76,77,3,12,6,0,77,78,5,6,0,0,78,11,1,0,0,0,79,84,3,14,
        7,0,80,81,5,22,0,0,81,83,3,14,7,0,82,80,1,0,0,0,83,86,1,0,0,0,84,
        82,1,0,0,0,84,85,1,0,0,0,85,13,1,0,0,0,86,84,1,0,0,0,87,94,3,16,
        8,0,88,94,3,18,9,0,89,94,3,20,10,0,90,94,3,22,11,0,91,94,3,28,14,
        0,92,94,3,10,5,0,93,87,1,0,0,0,93,88,1,0,0,0,93,89,1,0,0,0,93,90,
        1,0,0,0,93,91,1,0,0,0,93,92,1,0,0,0,94,15,1,0,0,0,95,96,5,14,0,0,
        96,97,3,30,15,0,97,98,5,15,0,0,98,101,3,14,7,0,99,100,5,16,0,0,100,
        102,3,14,7,0,101,99,1,0,0,0,101,102,1,0,0,0,102,17,1,0,0,0,103,104,
        5,7,0,0,104,105,3,30,15,0,105,106,5,8,0,0,106,107,3,14,7,0,107,19,
        1,0,0,0,108,109,5,9,0,0,109,110,5,26,0,0,110,111,3,6,3,0,111,112,
        5,27,0,0,112,21,1,0,0,0,113,114,5,13,0,0,114,115,5,26,0,0,115,116,
        3,24,12,0,116,117,5,27,0,0,117,23,1,0,0,0,118,123,3,26,13,0,119,
        120,5,25,0,0,120,122,3,26,13,0,121,119,1,0,0,0,122,125,1,0,0,0,123,
        121,1,0,0,0,123,124,1,0,0,0,124,25,1,0,0,0,125,123,1,0,0,0,126,129,
        3,30,15,0,127,129,5,29,0,0,128,126,1,0,0,0,128,127,1,0,0,0,129,27,
        1,0,0,0,130,131,5,31,0,0,131,132,5,28,0,0,132,133,3,30,15,0,133,
        29,1,0,0,0,134,135,3,32,16,0,135,31,1,0,0,0,136,141,3,34,17,0,137,
        138,5,19,0,0,138,140,3,34,17,0,139,137,1,0,0,0,140,143,1,0,0,0,141,
        139,1,0,0,0,141,142,1,0,0,0,142,33,1,0,0,0,143,141,1,0,0,0,144,147,
        3,36,18,0,145,146,5,21,0,0,146,148,3,36,18,0,147,145,1,0,0,0,147,
        148,1,0,0,0,148,35,1,0,0,0,149,154,3,38,19,0,150,151,5,17,0,0,151,
        153,3,38,19,0,152,150,1,0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,154,
        155,1,0,0,0,155,37,1,0,0,0,156,154,1,0,0,0,157,162,3,40,20,0,158,
        159,5,18,0,0,159,161,3,40,20,0,160,158,1,0,0,0,161,164,1,0,0,0,162,
        160,1,0,0,0,162,163,1,0,0,0,163,39,1,0,0,0,164,162,1,0,0,0,165,166,
        5,20,0,0,166,171,3,40,20,0,167,168,5,17,0,0,168,171,3,40,20,0,169,
        171,3,42,21,0,170,165,1,0,0,0,170,167,1,0,0,0,170,169,1,0,0,0,171,
        41,1,0,0,0,172,181,5,31,0,0,173,181,5,30,0,0,174,181,5,12,0,0,175,
        181,5,11,0,0,176,177,5,26,0,0,177,178,3,30,15,0,178,179,5,27,0,0,
        179,181,1,0,0,0,180,172,1,0,0,0,180,173,1,0,0,0,180,174,1,0,0,0,
        180,175,1,0,0,0,180,176,1,0,0,0,181,43,1,0,0,0,14,48,58,70,84,93,
        101,123,128,141,147,154,162,170,180
    ]

class CompiladorParser ( Parser ):

    grammarFileName = "Compilador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'~'", "<INVALID>", "';'", "'.'", "':'", "','", "'('", 
                     "')'", "':='" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "INTEGER", "BOOLEAN", "STRING", 
                      "BEGIN", "END", "WHILE", "DO", "READ", "VAR", "FALSE", 
                      "TRUE", "WRITE", "IF", "THEN", "ELSE", "OPAD", "OPMULT", 
                      "OPLOG", "OPNEG", "OPREL", "PVIG", "PONTO", "DPONTOS", 
                      "VIG", "ABPAR", "FPAR", "ATRIB", "CADEIA", "CTE", 
                      "ID", "COMMENT", "WS", "UNCLOSED_STRING", "ERROR_CHAR" ]

    RULE_programa = 0
    RULE_decls = 1
    RULE_declTip = 2
    RULE_listId = 3
    RULE_tip = 4
    RULE_cmdComp = 5
    RULE_listCmd = 6
    RULE_cmd = 7
    RULE_cmdIf = 8
    RULE_cmdWhile = 9
    RULE_cmdRead = 10
    RULE_cmdWrite = 11
    RULE_listW = 12
    RULE_elemW = 13
    RULE_cmdAtrib = 14
    RULE_expr = 15
    RULE_logicExpr = 16
    RULE_relationalExpr = 17
    RULE_additiveExpr = 18
    RULE_multiplicativeExpr = 19
    RULE_unaryExpr = 20
    RULE_primaryExpr = 21

    ruleNames =  [ "programa", "decls", "declTip", "listId", "tip", "cmdComp", 
                   "listCmd", "cmd", "cmdIf", "cmdWhile", "cmdRead", "cmdWrite", 
                   "listW", "elemW", "cmdAtrib", "expr", "logicExpr", "relationalExpr", 
                   "additiveExpr", "multiplicativeExpr", "unaryExpr", "primaryExpr" ]

    EOF = Token.EOF
    PROGRAM=1
    INTEGER=2
    BOOLEAN=3
    STRING=4
    BEGIN=5
    END=6
    WHILE=7
    DO=8
    READ=9
    VAR=10
    FALSE=11
    TRUE=12
    WRITE=13
    IF=14
    THEN=15
    ELSE=16
    OPAD=17
    OPMULT=18
    OPLOG=19
    OPNEG=20
    OPREL=21
    PVIG=22
    PONTO=23
    DPONTOS=24
    VIG=25
    ABPAR=26
    FPAR=27
    ATRIB=28
    CADEIA=29
    CTE=30
    ID=31
    COMMENT=32
    WS=33
    UNCLOSED_STRING=34
    ERROR_CHAR=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(CompiladorParser.PROGRAM, 0)

        def ID(self):
            return self.getToken(CompiladorParser.ID, 0)

        def PVIG(self):
            return self.getToken(CompiladorParser.PVIG, 0)

        def cmdComp(self):
            return self.getTypedRuleContext(CompiladorParser.CmdCompContext,0)


        def PONTO(self):
            return self.getToken(CompiladorParser.PONTO, 0)

        def EOF(self):
            return self.getToken(CompiladorParser.EOF, 0)

        def decls(self):
            return self.getTypedRuleContext(CompiladorParser.DeclsContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = CompiladorParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(CompiladorParser.PROGRAM)
            self.state = 45
            self.match(CompiladorParser.ID)
            self.state = 46
            self.match(CompiladorParser.PVIG)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 47
                self.decls()


            self.state = 50
            self.cmdComp()
            self.state = 51
            self.match(CompiladorParser.PONTO)
            self.state = 52
            self.match(CompiladorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CompiladorParser.VAR, 0)

        def declTip(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.DeclTipContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.DeclTipContext,i)


        def getRuleIndex(self):
            return CompiladorParser.RULE_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecls" ):
                listener.enterDecls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecls" ):
                listener.exitDecls(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = CompiladorParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(CompiladorParser.VAR)
            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.declTip()
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclTipContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listId(self):
            return self.getTypedRuleContext(CompiladorParser.ListIdContext,0)


        def DPONTOS(self):
            return self.getToken(CompiladorParser.DPONTOS, 0)

        def tip(self):
            return self.getTypedRuleContext(CompiladorParser.TipContext,0)


        def PVIG(self):
            return self.getToken(CompiladorParser.PVIG, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_declTip

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclTip" ):
                listener.enterDeclTip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclTip" ):
                listener.exitDeclTip(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclTip" ):
                return visitor.visitDeclTip(self)
            else:
                return visitor.visitChildren(self)




    def declTip(self):

        localctx = CompiladorParser.DeclTipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declTip)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.listId()
            self.state = 61
            self.match(CompiladorParser.DPONTOS)
            self.state = 62
            self.tip()
            self.state = 63
            self.match(CompiladorParser.PVIG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.ID)
            else:
                return self.getToken(CompiladorParser.ID, i)

        def VIG(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.VIG)
            else:
                return self.getToken(CompiladorParser.VIG, i)

        def getRuleIndex(self):
            return CompiladorParser.RULE_listId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListId" ):
                listener.enterListId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListId" ):
                listener.exitListId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListId" ):
                return visitor.visitListId(self)
            else:
                return visitor.visitChildren(self)




    def listId(self):

        localctx = CompiladorParser.ListIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_listId)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(CompiladorParser.ID)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 66
                self.match(CompiladorParser.VIG)
                self.state = 67
                self.match(CompiladorParser.ID)
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(CompiladorParser.INTEGER, 0)

        def BOOLEAN(self):
            return self.getToken(CompiladorParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(CompiladorParser.STRING, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_tip

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTip" ):
                listener.enterTip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTip" ):
                listener.exitTip(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTip" ):
                return visitor.visitTip(self)
            else:
                return visitor.visitChildren(self)




    def tip(self):

        localctx = CompiladorParser.TipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tip)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdCompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(CompiladorParser.BEGIN, 0)

        def listCmd(self):
            return self.getTypedRuleContext(CompiladorParser.ListCmdContext,0)


        def END(self):
            return self.getToken(CompiladorParser.END, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_cmdComp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdComp" ):
                listener.enterCmdComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdComp" ):
                listener.exitCmdComp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdComp" ):
                return visitor.visitCmdComp(self)
            else:
                return visitor.visitChildren(self)




    def cmdComp(self):

        localctx = CompiladorParser.CmdCompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cmdComp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(CompiladorParser.BEGIN)
            self.state = 76
            self.listCmd()
            self.state = 77
            self.match(CompiladorParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.CmdContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.CmdContext,i)


        def PVIG(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.PVIG)
            else:
                return self.getToken(CompiladorParser.PVIG, i)

        def getRuleIndex(self):
            return CompiladorParser.RULE_listCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListCmd" ):
                listener.enterListCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListCmd" ):
                listener.exitListCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListCmd" ):
                return visitor.visitListCmd(self)
            else:
                return visitor.visitChildren(self)




    def listCmd(self):

        localctx = CompiladorParser.ListCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_listCmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.cmd()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 80
                self.match(CompiladorParser.PVIG)
                self.state = 81
                self.cmd()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmdIf(self):
            return self.getTypedRuleContext(CompiladorParser.CmdIfContext,0)


        def cmdWhile(self):
            return self.getTypedRuleContext(CompiladorParser.CmdWhileContext,0)


        def cmdRead(self):
            return self.getTypedRuleContext(CompiladorParser.CmdReadContext,0)


        def cmdWrite(self):
            return self.getTypedRuleContext(CompiladorParser.CmdWriteContext,0)


        def cmdAtrib(self):
            return self.getTypedRuleContext(CompiladorParser.CmdAtribContext,0)


        def cmdComp(self):
            return self.getTypedRuleContext(CompiladorParser.CmdCompContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd" ):
                listener.enterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd" ):
                listener.exitCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd" ):
                return visitor.visitCmd(self)
            else:
                return visitor.visitChildren(self)




    def cmd(self):

        localctx = CompiladorParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cmd)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.cmdIf()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.cmdWhile()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.cmdRead()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.cmdWrite()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 5)
                self.state = 91
                self.cmdAtrib()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 92
                self.cmdComp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CompiladorParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(CompiladorParser.ExprContext,0)


        def THEN(self):
            return self.getToken(CompiladorParser.THEN, 0)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.CmdContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.CmdContext,i)


        def ELSE(self):
            return self.getToken(CompiladorParser.ELSE, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_cmdIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdIf" ):
                listener.enterCmdIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdIf" ):
                listener.exitCmdIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdIf" ):
                return visitor.visitCmdIf(self)
            else:
                return visitor.visitChildren(self)




    def cmdIf(self):

        localctx = CompiladorParser.CmdIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cmdIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(CompiladorParser.IF)
            self.state = 96
            self.expr()
            self.state = 97
            self.match(CompiladorParser.THEN)
            self.state = 98
            self.cmd()
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 99
                self.match(CompiladorParser.ELSE)
                self.state = 100
                self.cmd()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CompiladorParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(CompiladorParser.ExprContext,0)


        def DO(self):
            return self.getToken(CompiladorParser.DO, 0)

        def cmd(self):
            return self.getTypedRuleContext(CompiladorParser.CmdContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_cmdWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdWhile" ):
                listener.enterCmdWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdWhile" ):
                listener.exitCmdWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdWhile" ):
                return visitor.visitCmdWhile(self)
            else:
                return visitor.visitChildren(self)




    def cmdWhile(self):

        localctx = CompiladorParser.CmdWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cmdWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(CompiladorParser.WHILE)
            self.state = 104
            self.expr()
            self.state = 105
            self.match(CompiladorParser.DO)
            self.state = 106
            self.cmd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(CompiladorParser.READ, 0)

        def ABPAR(self):
            return self.getToken(CompiladorParser.ABPAR, 0)

        def listId(self):
            return self.getTypedRuleContext(CompiladorParser.ListIdContext,0)


        def FPAR(self):
            return self.getToken(CompiladorParser.FPAR, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_cmdRead

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdRead" ):
                listener.enterCmdRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdRead" ):
                listener.exitCmdRead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdRead" ):
                return visitor.visitCmdRead(self)
            else:
                return visitor.visitChildren(self)




    def cmdRead(self):

        localctx = CompiladorParser.CmdReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_cmdRead)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(CompiladorParser.READ)
            self.state = 109
            self.match(CompiladorParser.ABPAR)
            self.state = 110
            self.listId()
            self.state = 111
            self.match(CompiladorParser.FPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdWriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(CompiladorParser.WRITE, 0)

        def ABPAR(self):
            return self.getToken(CompiladorParser.ABPAR, 0)

        def listW(self):
            return self.getTypedRuleContext(CompiladorParser.ListWContext,0)


        def FPAR(self):
            return self.getToken(CompiladorParser.FPAR, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_cmdWrite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdWrite" ):
                listener.enterCmdWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdWrite" ):
                listener.exitCmdWrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdWrite" ):
                return visitor.visitCmdWrite(self)
            else:
                return visitor.visitChildren(self)




    def cmdWrite(self):

        localctx = CompiladorParser.CmdWriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_cmdWrite)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(CompiladorParser.WRITE)
            self.state = 114
            self.match(CompiladorParser.ABPAR)
            self.state = 115
            self.listW()
            self.state = 116
            self.match(CompiladorParser.FPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListWContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elemW(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.ElemWContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.ElemWContext,i)


        def VIG(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.VIG)
            else:
                return self.getToken(CompiladorParser.VIG, i)

        def getRuleIndex(self):
            return CompiladorParser.RULE_listW

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListW" ):
                listener.enterListW(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListW" ):
                listener.exitListW(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListW" ):
                return visitor.visitListW(self)
            else:
                return visitor.visitChildren(self)




    def listW(self):

        localctx = CompiladorParser.ListWContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_listW)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.elemW()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 119
                self.match(CompiladorParser.VIG)
                self.state = 120
                self.elemW()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElemWContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CompiladorParser.ExprContext,0)


        def CADEIA(self):
            return self.getToken(CompiladorParser.CADEIA, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_elemW

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElemW" ):
                listener.enterElemW(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElemW" ):
                listener.exitElemW(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElemW" ):
                return visitor.visitElemW(self)
            else:
                return visitor.visitChildren(self)




    def elemW(self):

        localctx = CompiladorParser.ElemWContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_elemW)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 17, 20, 26, 30, 31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.expr()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(CompiladorParser.CADEIA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdAtribContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CompiladorParser.ID, 0)

        def ATRIB(self):
            return self.getToken(CompiladorParser.ATRIB, 0)

        def expr(self):
            return self.getTypedRuleContext(CompiladorParser.ExprContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_cmdAtrib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdAtrib" ):
                listener.enterCmdAtrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdAtrib" ):
                listener.exitCmdAtrib(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdAtrib" ):
                return visitor.visitCmdAtrib(self)
            else:
                return visitor.visitChildren(self)




    def cmdAtrib(self):

        localctx = CompiladorParser.CmdAtribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_cmdAtrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(CompiladorParser.ID)
            self.state = 131
            self.match(CompiladorParser.ATRIB)
            self.state = 132
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicExpr(self):
            return self.getTypedRuleContext(CompiladorParser.LogicExprContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CompiladorParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.logicExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.RelationalExprContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.RelationalExprContext,i)


        def OPLOG(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.OPLOG)
            else:
                return self.getToken(CompiladorParser.OPLOG, i)

        def getRuleIndex(self):
            return CompiladorParser.RULE_logicExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicExpr" ):
                listener.enterLogicExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicExpr" ):
                listener.exitLogicExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicExpr" ):
                return visitor.visitLogicExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicExpr(self):

        localctx = CompiladorParser.LogicExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_logicExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.relationalExpr()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 137
                self.match(CompiladorParser.OPLOG)
                self.state = 138
                self.relationalExpr()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.AdditiveExprContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.AdditiveExprContext,i)


        def OPREL(self):
            return self.getToken(CompiladorParser.OPREL, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_relationalExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpr(self):

        localctx = CompiladorParser.RelationalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_relationalExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.additiveExpr()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 145
                self.match(CompiladorParser.OPREL)
                self.state = 146
                self.additiveExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.MultiplicativeExprContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.MultiplicativeExprContext,i)


        def OPAD(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.OPAD)
            else:
                return self.getToken(CompiladorParser.OPAD, i)

        def getRuleIndex(self):
            return CompiladorParser.RULE_additiveExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpr(self):

        localctx = CompiladorParser.AdditiveExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.multiplicativeExpr()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 150
                self.match(CompiladorParser.OPAD)
                self.state = 151
                self.multiplicativeExpr()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorParser.UnaryExprContext)
            else:
                return self.getTypedRuleContext(CompiladorParser.UnaryExprContext,i)


        def OPMULT(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorParser.OPMULT)
            else:
                return self.getToken(CompiladorParser.OPMULT, i)

        def getRuleIndex(self):
            return CompiladorParser.RULE_multiplicativeExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpr" ):
                listener.enterMultiplicativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpr" ):
                listener.exitMultiplicativeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpr(self):

        localctx = CompiladorParser.MultiplicativeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.unaryExpr()
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 158
                self.match(CompiladorParser.OPMULT)
                self.state = 159
                self.unaryExpr()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPNEG(self):
            return self.getToken(CompiladorParser.OPNEG, 0)

        def unaryExpr(self):
            return self.getTypedRuleContext(CompiladorParser.UnaryExprContext,0)


        def OPAD(self):
            return self.getToken(CompiladorParser.OPAD, 0)

        def primaryExpr(self):
            return self.getTypedRuleContext(CompiladorParser.PrimaryExprContext,0)


        def getRuleIndex(self):
            return CompiladorParser.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = CompiladorParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_unaryExpr)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(CompiladorParser.OPNEG)
                self.state = 166
                self.unaryExpr()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(CompiladorParser.OPAD)
                self.state = 168
                self.unaryExpr()
                pass
            elif token in [11, 12, 26, 30, 31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
                self.primaryExpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CompiladorParser.ID, 0)

        def CTE(self):
            return self.getToken(CompiladorParser.CTE, 0)

        def TRUE(self):
            return self.getToken(CompiladorParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CompiladorParser.FALSE, 0)

        def ABPAR(self):
            return self.getToken(CompiladorParser.ABPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(CompiladorParser.ExprContext,0)


        def FPAR(self):
            return self.getToken(CompiladorParser.FPAR, 0)

        def getRuleIndex(self):
            return CompiladorParser.RULE_primaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpr(self):

        localctx = CompiladorParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_primaryExpr)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(CompiladorParser.ID)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(CompiladorParser.CTE)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.match(CompiladorParser.TRUE)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 175
                self.match(CompiladorParser.FALSE)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 5)
                self.state = 176
                self.match(CompiladorParser.ABPAR)
                self.state = 177
                self.expr()
                self.state = 178
                self.match(CompiladorParser.FPAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





