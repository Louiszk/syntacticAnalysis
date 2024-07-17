# Documentation
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