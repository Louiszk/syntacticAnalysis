from parsimonious import Grammar, NodeVisitor
import re

#add comments
grammar = Grammar(r"""
    # One main function (other functions before)
    program = ws (function ws)* main_function ws

    function = "def" tws function_identifier "(" ws parameter_list? ws ")" tws
                   ((statement_list tws) / ws)
                   "return" tws ((argument_list tws) / ws)
                   "end"
                  
    main_function = "def main(" ws parameter_list? ws ")" tws
                   ((statement_list tws) / ws)
                   "return" tws ((argument_list tws) / ws)
                   "end"

    parameter_list = identifier (ws "," ws identifier)*
                  
    statement_list = statement (tws statement)*
    statement = assignment / conditional / loop / function_call
    
    #only allow function call as own statement or assignment
    assignment = parameter_list ws "=" ws (function_call / argument_list)

    # no nested expression with ()
    expression = arithmetic

    arithmetic = term (ws arithmetic_op ws term)*
    term = identifier / number
    arithmetic_op = "+" / "-" / "*" / "/"
                   
    conditional = "if" tws conditions tws statement_list (tws "else" tws statement_list)? tws "end"

    loop = "while" tws conditions tws statement_list tws "end"
    
    #no negations of conditions
    condition = expression ws comp ws expression
    comp = ">=" / "<=" / ">" / "<" / "==" / "!="
    conditions = condition (ws logical_op ws condition)*
    logical_op = "&&" / "||"

    function_call = function_identifier "(" ws argument_list? ws ")"
    argument_list = expression (ws "," ws expression)*   
                  
    reserved_words = "end" / "def" / "if" / "else" / "while"
    function_identifier =  !("main" / reserved_words) identifier         

    identifier = !reserved_words ~r"[A-Za-z][A-Za-z0-9]*"
    number = ~r"\d+"

    # conditional whitespace
    ws = ~r"\s*"
    # true whitespace
    tws = ~r"\s+"
""")



# Test Programs
test = '''
// test function
def bigTestFunction(x, y)
    // Initialize
    a, b = en(x * 2, y + 5)
    
    // Conditional statement
    if a > 10
        z = a * b, b*a
    else
        z = a + b
    end

    // Loop with nested function call /condition
    while z < 100
        if a > 10
            z = a / b
        else
            z = a - b
        end
        z = z + 1
        updateValue(z, x)
    end


    // Nested conditional with logical operators
    if x >= 0 && y <= 10 || z == 50
        temp = complexCalculation(x, y, z)
        if temp > 100
            result = result + High
        else
            result = result + Low
            while x<3
                x=x+1
                result  = result *3
            end
        end
    end

    return z, result, arr
end

def calculateValues(p, q)
    return p + q, p * q
end

// Main function
def main(arg1, arg2)
    finalZ, finalResult = bigTestFunction(arg1, arg2)
    printResults(finalZ, finalResult)
    return finalZ
end
/* this is the end of the program */
'''

test1 = '''
def multiply(a, b)
    result = a * b
    return result
end

def sumAndDifference(a, b)
    sum = a + b
    diff = a - b
    return sum, diff
end

def main(x, y)
    product = multiply(x, y)
    if product > 100
        message = 1
    else
        message, diff = sumAndDifference(x, y)
    end
    printResult(product, message)
    return product
end
'''

test2 = '''
def computeFactorial(n)
    fact = 1
    while n > 0
        fact = fact * n
        n = n - 1
    end
    return fact
end

def main(num)
    result = computeFactorial(num)
    print(result)
    return result
end
'''


# comments do not need to be parsed
def remove_comments(code):

    code = re.sub(r'/\*[\s\S]*?\*/', '', code)
    
    code = re.sub(r'//.*', '', code)
    
    return code

class TreePrinter(NodeVisitor):
    def print_tree(self, node, level=0):
        indent = "|  " * level
        if node.expr_name:
            print(f"{indent}{node.expr_name}:")
        
        if node.children:
            for child in node.children:
                self.print_tree(child, level + 1)
        else:
            print(f"{indent}  {node.text}")

if __name__ == "__main__":
    program = input("Please enter your program:")
    removed_comments = remove_comments(program)
    tree = grammar.parse(removed_comments)
    printer = TreePrinter()
    print(f"Parse tree for your program: \n")
    printer.print_tree(tree)
