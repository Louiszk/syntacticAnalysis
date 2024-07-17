# Generated from Calculator.g4 by ANTLR 4.13.1
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
        4,1,6,38,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,0,
        1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,24,8,2,1,3,1,3,1,4,1,4,1,
        4,3,4,31,8,4,1,5,1,5,1,5,3,5,36,8,5,1,5,0,0,6,0,2,4,6,8,10,0,0,34,
        0,12,1,0,0,0,2,15,1,0,0,0,4,23,1,0,0,0,6,25,1,0,0,0,8,30,1,0,0,0,
        10,35,1,0,0,0,12,13,3,2,1,0,13,14,3,8,4,0,14,1,1,0,0,0,15,16,3,4,
        2,0,16,17,3,10,5,0,17,3,1,0,0,0,18,24,3,6,3,0,19,20,5,1,0,0,20,21,
        3,0,0,0,21,22,5,2,0,0,22,24,1,0,0,0,23,18,1,0,0,0,23,19,1,0,0,0,
        24,5,1,0,0,0,25,26,5,5,0,0,26,7,1,0,0,0,27,28,5,3,0,0,28,31,3,0,
        0,0,29,31,1,0,0,0,30,27,1,0,0,0,30,29,1,0,0,0,31,9,1,0,0,0,32,33,
        5,4,0,0,33,36,3,2,1,0,34,36,1,0,0,0,35,32,1,0,0,0,35,34,1,0,0,0,
        36,11,1,0,0,0,3,23,30,35
    ]

class CalculatorParser ( Parser ):

    grammarFileName = "Calculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "WS" ]

    RULE_exp = 0
    RULE_term = 1
    RULE_factor = 2
    RULE_literal = 3
    RULE_exp_ = 4
    RULE_term_ = 5

    ruleNames =  [ "exp", "term", "factor", "literal", "exp_", "term_" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NUMBER=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(CalculatorParser.TermContext,0)


        def exp_(self):
            return self.getTypedRuleContext(CalculatorParser.Exp_Context,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = CalculatorParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.term()
            self.state = 13
            self.exp_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(CalculatorParser.FactorContext,0)


        def term_(self):
            return self.getTypedRuleContext(CalculatorParser.Term_Context,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = CalculatorParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.factor()
            self.state = 16
            self.term_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(CalculatorParser.LiteralContext,0)


        def exp(self):
            return self.getTypedRuleContext(CalculatorParser.ExpContext,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = CalculatorParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.literal()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(CalculatorParser.T__0)
                self.state = 20
                self.exp()
                self.state = 21
                self.match(CalculatorParser.T__1)
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(CalculatorParser.NUMBER, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CalculatorParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(CalculatorParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(CalculatorParser.ExpContext,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_exp_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_" ):
                return visitor.visitExp_(self)
            else:
                return visitor.visitChildren(self)




    def exp_(self):

        localctx = CalculatorParser.Exp_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exp_)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(CalculatorParser.T__2)
                self.state = 28
                self.exp()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)

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


    class Term_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(CalculatorParser.TermContext,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_term_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_" ):
                return visitor.visitTerm_(self)
            else:
                return visitor.visitChildren(self)




    def term_(self):

        localctx = CalculatorParser.Term_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_term_)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(CalculatorParser.T__3)
                self.state = 33
                self.term()
                pass
            elif token in [2, 3]:
                self.enterOuterAlt(localctx, 2)

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





