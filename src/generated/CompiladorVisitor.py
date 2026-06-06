# Generated from grammar/Compilador.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CompiladorParser import CompiladorParser
else:
    from CompiladorParser import CompiladorParser

# This class defines a complete generic visitor for a parse tree produced by CompiladorParser.

class CompiladorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CompiladorParser#programa.
    def visitPrograma(self, ctx:CompiladorParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#decls.
    def visitDecls(self, ctx:CompiladorParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#declTip.
    def visitDeclTip(self, ctx:CompiladorParser.DeclTipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#listId.
    def visitListId(self, ctx:CompiladorParser.ListIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#tip.
    def visitTip(self, ctx:CompiladorParser.TipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#cmdComp.
    def visitCmdComp(self, ctx:CompiladorParser.CmdCompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#listCmd.
    def visitListCmd(self, ctx:CompiladorParser.ListCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#cmd.
    def visitCmd(self, ctx:CompiladorParser.CmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#cmdIf.
    def visitCmdIf(self, ctx:CompiladorParser.CmdIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#cmdWhile.
    def visitCmdWhile(self, ctx:CompiladorParser.CmdWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#cmdRead.
    def visitCmdRead(self, ctx:CompiladorParser.CmdReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#cmdWrite.
    def visitCmdWrite(self, ctx:CompiladorParser.CmdWriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#listW.
    def visitListW(self, ctx:CompiladorParser.ListWContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#elemW.
    def visitElemW(self, ctx:CompiladorParser.ElemWContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#cmdAtrib.
    def visitCmdAtrib(self, ctx:CompiladorParser.CmdAtribContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#expr.
    def visitExpr(self, ctx:CompiladorParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#logicExpr.
    def visitLogicExpr(self, ctx:CompiladorParser.LogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#relationalExpr.
    def visitRelationalExpr(self, ctx:CompiladorParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:CompiladorParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:CompiladorParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#unaryExpr.
    def visitUnaryExpr(self, ctx:CompiladorParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:CompiladorParser.PrimaryExprContext):
        return self.visitChildren(ctx)



del CompiladorParser