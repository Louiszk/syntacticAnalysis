from antlr4 import *
from CalculatorLexer import CalculatorLexer
from CalculatorParser import CalculatorParser
from dash import Dash, html,  dcc, Input, Output, State, no_update
import dash_cytoscape as cyto
import sys 
import io

#get parsing tree via Antlr
def get_tree(expression):
    stderr_buffer = io.StringIO()
    sys.stderr = stderr_buffer

    lexer = CalculatorLexer(InputStream(expression))
    stream = CommonTokenStream(lexer)
    parser = CalculatorParser(stream)
    tree = parser.exp()
    
    output = stderr_buffer.getvalue()
    sys.stderr = sys.__stderr__

    return tree, parser.ruleNames, output

#Calculate the solution of the expression
class EvalVisitor(ParseTreeVisitor):
    def visitExp(self, ctx:CalculatorParser.ExpContext):

        if ctx.getChild(1).getChildCount()==2:

            left = self.visit(ctx.term())
            right = self.visit(ctx.exp_())
        
            return left + right
        
        else:
            return self.visit(ctx.term())
        

    def visitTerm(self, ctx:CalculatorParser.TermContext):
        if ctx.getChild(1).getChildCount()==2:

            left = self.visit(ctx.factor())
            right = self.visit(ctx.term_())
        
            return left * right
        else:
            return self.visit(ctx.factor())
        

    def visitFactor(self, ctx:CalculatorParser.FactorContext):
        if ctx.getChildCount() == 1:        
            return self.visit(ctx.literal())  
        else:
            return self.visit(ctx.exp())

    def visitLiteral(self, ctx:CalculatorParser.LiteralContext):
        return int(ctx.NUMBER().getText())

    def visitExp_(self, ctx:CalculatorParser.Exp_Context):
        return self.visit(ctx.exp())

    def visitTerm_(self, ctx:CalculatorParser.Term_Context):
        return self.visit(ctx.term())

def calculate_solution(tree):
    visitor = EvalVisitor()
    try:
        return visitor.visit(tree)
    except Exception as e:
        print("An Error occurred", e)
        return None
    
#Visualization
app = Dash(__name__, title="Lab01", external_scripts = [{"src": "https://cdn.tailwindcss.com"}])

stylesheet = [
            {
                'selector': 'node',
                'style': {
                    'shape': 'round-rectangle',
                    'label': 'data(label)',
                    'font-size': '30px',
                    'text-valign': 'center',
                    'text-halign': 'center',
                    'color': 'black',
                    'text-outline-width': '1px',
                    "text-wrap": "wrap",
                    'background-color': 'white',
                    'width': '80px',
                    'height': '40px',
                    "text-wrap": "wrap"
                }},
            {
                'selector': '.NT',
                'style': {    
                    'border-width': '4px',
                    'border-color': '#FF584C',
                }},
            {
                'selector': '.T',
                'style': {    
                    'border-width': '6px',
                    'border-color': '#86FF84',
                    'width': '160px',
                    'height': '80px',
                    'font-size': '60px',
                }},
            {
                'selector': '.e',
                'style': {    
                    'border-width': '6px',
                    'border-color': '#86FF84',
                    'width': '80px',
                    'height': '40px',
                    'font-size': '60px',
                }},
                {
                'selector': 'edge',
                'style': {
                    'line-color': 'black',
                    'width': '5px'
                }}
]
app.layout = html.Div([
    html.Div([
        html.Button("Calculate", id = 'calculate', className = 'rounded-md px-2 py-2 border-2 border-green-600 bg-green-200 h-12'),
        dcc.Input(value = '3+3', id = 'expression', className = 'border-2 border-zinc-800 rounded-md'),
        html.Div("=", className = 'font-bold text-4xl'),
        html.H1(id = 'solution', className = 'font-bold text-4xl')
    ], className = 'flex flex-row gap-3 font-semibold text-zinc-700'),
    html.Div(id = "output", className = 'font-semibold text-red-400'),
    cyto.Cytoscape(
            id='tree',
            minZoom=0.01,
            maxZoom=0.5,    
            autoungrabify = True,
            boxSelectionEnabled = True,
            style={'width': '80%', 'height': '600px'},
            elements=[],
            stylesheet= stylesheet,
            layout={'name': 'preset', 'animate':True}
            )
], className = 'flex flex-col gap-4 m-4 overflow-y-scroll items-center')

#Calculation Callback
@app.callback(
        Output('tree', 'elements'),
        Output('solution', 'children'),
        Output('output', 'children'),
        Input('calculate', 'n_clicks'),
        Input('expression', 'n_submit'),
        State('expression', 'value'),
        prevent_initial_call = True
)
def calculate(n, n2, expression):
    if not n and not n2:
        return no_update, no_update, no_update
    
    tree, rule_names, output = get_tree(expression)

    #output errors
    output_div = []
    output = output.split("line")
    for i in range(len(output)):
        if 'no viable alternative at input' not in output[i]:
            output_div.append(html.Div(output[i]))

    solution = calculate_solution(tree)

    if not solution:
        return [{'data':{'id':'error', 'label':'Error while Parsing :/'}}], 'NaN', output_div
    
    #get max depth to display tree better
    max_depth = 0

    def tree_depth(node, depth):
        nonlocal max_depth

        if isinstance(node, ParserRuleContext):
            max_depth = max(max_depth, depth)
            for i in range(node.getChildCount()):
                tree_depth(node.getChild(i), depth + 1)

    
    tree_depth(tree, 0)

    #Filling Nodes and Edges for Cytoscape viz
    nodes = []
    edges = []

    id_counter = 0

    def traverse_tree(node, step, x, parent=None):
        
        nonlocal id_counter

        node_id = id_counter
        text = rule_names[node.getRuleIndex()] if isinstance(node, ParserRuleContext) else node.getText()
        text = '( exp )' if text == ')' else text
        nodeclass = 'NT' if isinstance(node, ParserRuleContext) else 'T'
        nodes.append({
                'data': {'id': str(node_id), 'label': text},
                'position': {'x': x, 'y': step*140},
                'classes': nodeclass
            })
        id_counter += 1

        if parent is not None:
            edges.append({'data':{'source': str(parent), 'target': str(node_id)}})

        
        if isinstance(node, ParserRuleContext):
            amount_children = node.getChildCount()
            if amount_children==0:
                nodes.append({
                'data': {'id': f'epsilon_{node_id}', 'label': 'ε'},
                'position': {'x': x, 'y': (step+1)*140},
                'classes': 'e'
                })
                edges.append({'data':{'source': str(node_id), 'target': f'epsilon_{node_id}'}})

            for i in range(amount_children):
                if amount_children==2:
                    x_new = x - (max_depth-step)*120*(1-step/max_depth) if i==0 else x + (max_depth-step)*120*(1-step/max_depth)
                else:
                    x_new = x
                traverse_tree(node.getChild(i), step+1, x_new, node_id)
        

    # Start traversing the tree
    traverse_tree(tree, 0, 0)
    

    return nodes + edges, solution, output_div

if __name__ == '__main__':
    app.run_server(debug=True)




