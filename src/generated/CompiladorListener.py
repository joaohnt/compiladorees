# Generated from grammar/Compilador.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CompiladorParser import CompiladorParser
else:
    from CompiladorParser import CompiladorParser

# This class defines a complete listener for a parse tree produced by CompiladorParser.
class CompiladorListener(ParseTreeListener):

    # Enter a parse tree produced by CompiladorParser#programa.
    def enterPrograma(self, ctx:CompiladorParser.ProgramaContext):
        pass

    # Exit a parse tree produced by CompiladorParser#programa.
    def exitPrograma(self, ctx:CompiladorParser.ProgramaContext):
        pass


    # Enter a parse tree produced by CompiladorParser#decls.
    def enterDecls(self, ctx:CompiladorParser.DeclsContext):
        pass

    # Exit a parse tree produced by CompiladorParser#decls.
    def exitDecls(self, ctx:CompiladorParser.DeclsContext):
        pass


    # Enter a parse tree produced by CompiladorParser#declTip.
    def enterDeclTip(self, ctx:CompiladorParser.DeclTipContext):
        pass

    # Exit a parse tree produced by CompiladorParser#declTip.
    def exitDeclTip(self, ctx:CompiladorParser.DeclTipContext):
        pass


    # Enter a parse tree produced by CompiladorParser#listId.
    def enterListId(self, ctx:CompiladorParser.ListIdContext):
        pass

    # Exit a parse tree produced by CompiladorParser#listId.
    def exitListId(self, ctx:CompiladorParser.ListIdContext):
        pass


    # Enter a parse tree produced by CompiladorParser#tip.
    def enterTip(self, ctx:CompiladorParser.TipContext):
        pass

    # Exit a parse tree produced by CompiladorParser#tip.
    def exitTip(self, ctx:CompiladorParser.TipContext):
        pass


    # Enter a parse tree produced by CompiladorParser#cmdComp.
    def enterCmdComp(self, ctx:CompiladorParser.CmdCompContext):
        pass

    # Exit a parse tree produced by CompiladorParser#cmdComp.
    def exitCmdComp(self, ctx:CompiladorParser.CmdCompContext):
        pass


    # Enter a parse tree produced by CompiladorParser#listCmd.
    def enterListCmd(self, ctx:CompiladorParser.ListCmdContext):
        pass

    # Exit a parse tree produced by CompiladorParser#listCmd.
    def exitListCmd(self, ctx:CompiladorParser.ListCmdContext):
        pass


    # Enter a parse tree produced by CompiladorParser#cmd.
    def enterCmd(self, ctx:CompiladorParser.CmdContext):
        pass

    # Exit a parse tree produced by CompiladorParser#cmd.
    def exitCmd(self, ctx:CompiladorParser.CmdContext):
        pass


    # Enter a parse tree produced by CompiladorParser#cmdIf.
    def enterCmdIf(self, ctx:CompiladorParser.CmdIfContext):
        pass

    # Exit a parse tree produced by CompiladorParser#cmdIf.
    def exitCmdIf(self, ctx:CompiladorParser.CmdIfContext):
        pass


    # Enter a parse tree produced by CompiladorParser#cmdWhile.
    def enterCmdWhile(self, ctx:CompiladorParser.CmdWhileContext):
        pass

    # Exit a parse tree produced by CompiladorParser#cmdWhile.
    def exitCmdWhile(self, ctx:CompiladorParser.CmdWhileContext):
        pass


    # Enter a parse tree produced by CompiladorParser#cmdRead.
    def enterCmdRead(self, ctx:CompiladorParser.CmdReadContext):
        pass

    # Exit a parse tree produced by CompiladorParser#cmdRead.
    def exitCmdRead(self, ctx:CompiladorParser.CmdReadContext):
        pass


    # Enter a parse tree produced by CompiladorParser#cmdWrite.
    def enterCmdWrite(self, ctx:CompiladorParser.CmdWriteContext):
        pass

    # Exit a parse tree produced by CompiladorParser#cmdWrite.
    def exitCmdWrite(self, ctx:CompiladorParser.CmdWriteContext):
        pass


    # Enter a parse tree produced by CompiladorParser#listW.
    def enterListW(self, ctx:CompiladorParser.ListWContext):
        pass

    # Exit a parse tree produced by CompiladorParser#listW.
    def exitListW(self, ctx:CompiladorParser.ListWContext):
        pass


    # Enter a parse tree produced by CompiladorParser#elemW.
    def enterElemW(self, ctx:CompiladorParser.ElemWContext):
        pass

    # Exit a parse tree produced by CompiladorParser#elemW.
    def exitElemW(self, ctx:CompiladorParser.ElemWContext):
        pass


    # Enter a parse tree produced by CompiladorParser#cmdAtrib.
    def enterCmdAtrib(self, ctx:CompiladorParser.CmdAtribContext):
        pass

    # Exit a parse tree produced by CompiladorParser#cmdAtrib.
    def exitCmdAtrib(self, ctx:CompiladorParser.CmdAtribContext):
        pass


    # Enter a parse tree produced by CompiladorParser#expr.
    def enterExpr(self, ctx:CompiladorParser.ExprContext):
        pass

    # Exit a parse tree produced by CompiladorParser#expr.
    def exitExpr(self, ctx:CompiladorParser.ExprContext):
        pass


    # Enter a parse tree produced by CompiladorParser#logicExpr.
    def enterLogicExpr(self, ctx:CompiladorParser.LogicExprContext):
        pass

    # Exit a parse tree produced by CompiladorParser#logicExpr.
    def exitLogicExpr(self, ctx:CompiladorParser.LogicExprContext):
        pass


    # Enter a parse tree produced by CompiladorParser#relationalExpr.
    def enterRelationalExpr(self, ctx:CompiladorParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by CompiladorParser#relationalExpr.
    def exitRelationalExpr(self, ctx:CompiladorParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by CompiladorParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:CompiladorParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by CompiladorParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:CompiladorParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by CompiladorParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:CompiladorParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by CompiladorParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:CompiladorParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by CompiladorParser#unaryExpr.
    def enterUnaryExpr(self, ctx:CompiladorParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by CompiladorParser#unaryExpr.
    def exitUnaryExpr(self, ctx:CompiladorParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by CompiladorParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:CompiladorParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by CompiladorParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:CompiladorParser.PrimaryExprContext):
        pass



del CompiladorParser