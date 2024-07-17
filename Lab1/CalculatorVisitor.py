# Generated from Calculator.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete generic visitor for a parse tree produced by CalculatorParser.

class CalculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculatorParser#exp.
    def visitExp(self, ctx:CalculatorParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#term.
    def visitTerm(self, ctx:CalculatorParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#factor.
    def visitFactor(self, ctx:CalculatorParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#literal.
    def visitLiteral(self, ctx:CalculatorParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#exp_.
    def visitExp_(self, ctx:CalculatorParser.Exp_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#term_.
    def visitTerm_(self, ctx:CalculatorParser.Term_Context):
        return self.visitChildren(ctx)



del CalculatorParser