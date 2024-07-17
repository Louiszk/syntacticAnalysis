from antlr4 import *
from AmbiguousLexer import AmbiguousLexer
from AmbiguousParser import AmbiguousParser
import sys

class EvalVisitor(ParseTreeVisitor):
    def visitexp(self, ctx:AmbiguousParser.ExpContext):
        print("hello")
        print(ctx)
   

def calculate_solution(tree):
    visitor = EvalVisitor()
    return visitor.visit(tree)

def main():
    my_input = "L+I"
    lexer = AmbiguousLexer(InputStream(my_input))
    stream = CommonTokenStream(lexer)
    parser = AmbiguousParser(stream)
    tree = parser.exp()
    print(tree.toStringTree(recog=parser))
    calculate_solution(tree)

if __name__ == '__main__':
    main()