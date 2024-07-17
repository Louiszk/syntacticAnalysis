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
