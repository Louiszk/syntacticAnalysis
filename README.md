# University Module called Syntactic Analysis

# Lab01 - LL(k)

I used ANTLR lexer and parser in Python. I began by copying the LL(1) grammar from the lecture (without Id) and put it in Calculator.g4.
ANTLR4 uses LL(*) for parsing, but it would only need a lookahead of one.
I installed antlr4 with `pip install antlr4-python3-runtime`.
Then 'compiled' it with `antlr4 -Dlanguage=Python3 -no-listener -visitor Calculator.g4`

For visualization and interaction, I leveraged Dash for a web-based interface. Install it via `pip install dash` and `pip install dash-cytoscape`.
Then run calculator.py and open your webbrowser at http://127.0.0.1:8050/

The calculations allow Multiplication *, Addition +, with parantheses over the natural Numbers.
Additionally the parsing Tree gets traversed and displayed with cytoscape. You can zoom and pan the graph.
(Unfortunately, for large trees lines may cross. I could have increased the x distance but then the trees get even wider (with potential whitespace).)
I also managed to redirect the errors from console to the dashboard.

# Lab03 - PEG

## Structure
- program [subset of ruby (almost)] consists any number of function definitions and one main function at the end (named main)
- you can call every function except main

## Syntax Overview
- **Comments:** 
  - Single-line comments: `//`
  - Multi-line comments: `/* ... */`
- **Whitespace:**
  - allowed almost everywhere (ws) and sometimes required (tws)
- **Functions**
    ```
    def functionName(param1, param2, ...)
        statement1
        statement2
        ...
        return output1, output2, ...
    end
    ```
- **Statements**
  - functioncalls
  - assignments:
    - a, d = 2 * b, 3 * 4
    - a, b = myfunction(c)
  - conditionals:
    - if 3 < 4 && 3==a || 4<1 b = c function1call(v *4, c) else a = b end
  - while-loops:
    - while x!=4 x=x+1 function2call(x * x * 3) end
  - assignments can be nested in conditionals and while-loops
  - while-loops and conditionals can be inside while-loops and conditionals
  
## Drawbacks
- Expressions and logical operators can not be nested (with parantheses)
- therefore there is also no negation possible
- function calls are only possible as own statement or assignment
- function definitions are restricted inside functions
- no strings, conditions as variables
- no assignments as conditionals

## Examples
- grammar is provided in source code
- examples are given in the source code (test, test1, test2) (all tests work)

## Choice of Parser
- [Parsimonious](https://github.com/erikrose/parsimonious) - "the fastest pure-Python PEG parser"
- EBNF-like notation to define grammars (allows regex)
- removing comments before parsing
