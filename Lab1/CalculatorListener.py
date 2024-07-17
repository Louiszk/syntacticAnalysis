# Generated from Calculator.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete listener for a parse tree produced by CalculatorParser.
class CalculatorListener(ParseTreeListener):

    # Enter a parse tree produced by CalculatorParser#exp.
    def enterExp(self, ctx:CalculatorParser.ExpContext):
        pass

    # Exit a parse tree produced by CalculatorParser#exp.
    def exitExp(self, ctx:CalculatorParser.ExpContext):
        pass


    # Enter a parse tree produced by CalculatorParser#term.
    def enterTerm(self, ctx:CalculatorParser.TermContext):
        pass

    # Exit a parse tree produced by CalculatorParser#term.
    def exitTerm(self, ctx:CalculatorParser.TermContext):
        pass


    # Enter a parse tree produced by CalculatorParser#factor.
    def enterFactor(self, ctx:CalculatorParser.FactorContext):
        pass

    # Exit a parse tree produced by CalculatorParser#factor.
    def exitFactor(self, ctx:CalculatorParser.FactorContext):
        pass


    # Enter a parse tree produced by CalculatorParser#literal.
    def enterLiteral(self, ctx:CalculatorParser.LiteralContext):
        pass

    # Exit a parse tree produced by CalculatorParser#literal.
    def exitLiteral(self, ctx:CalculatorParser.LiteralContext):
        pass


    # Enter a parse tree produced by CalculatorParser#exp_.
    def enterExp_(self, ctx:CalculatorParser.Exp_Context):
        pass

    # Exit a parse tree produced by CalculatorParser#exp_.
    def exitExp_(self, ctx:CalculatorParser.Exp_Context):
        pass


    # Enter a parse tree produced by CalculatorParser#term_.
    def enterTerm_(self, ctx:CalculatorParser.Term_Context):
        pass

    # Exit a parse tree produced by CalculatorParser#term_.
    def exitTerm_(self, ctx:CalculatorParser.Term_Context):
        pass



del CalculatorParser