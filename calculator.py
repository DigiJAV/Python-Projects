"""
Order Operators are Evaluated
    1Parenthesis
    2Exponents
    3Multiplication, modulo, Division
    4Addition, subtraction 
 

    (7 + 3) * (12 - 4) / (2 ^ 3)                output: 10                      P
    15 - (9 * 4) + (6 ^ 2) / 3                  out:    -9                      P
    (8 + 2) * (5 - 1) ^ 2 / (4 + 2)             out:    26.6666666666666666     PASS
    20 - (3 * 4) + (7 ^ 2) - (10 / 2)           out:    52                      PASS
    (11 + 4) * (6 - 2) / (3 ^ 2) + 5            out:    11.6666666666           PASS
    18 - (5 * 3) + (9 ^ 2) / (8 / 2)            out:    23.25                   PASS
    (13 + 2) * (8 - 4) ^ 2 / (6 + 1)            out:    34.2857142857           PASS
    25 - (7 * 2) + (4 ^ 3) - (12 / 3)           out:    71                      PASS
    (17 + 3) * (10 - 3) / (5 ^ 2) + 2                   7.6                     PASS
    22 - (6 * 4) + (11 ^ 2) / (9 / 3)                   38.333333333333         PASS
    (7 +^ 3) * (12 -/ 4) / (2 ^+ 3)                     error                   PASS  
              
    (7 + 3) * (12 - 4) / (0)                            error                   P
    -(2 + 3)                                            -5                      P
    5 + 3 )                                             error                   P
    ( 4 - 2                                             error                   P
    5 + * 3                                             error                   P
    5 / 0 + 2                                           error                   P
    
    + 2 * 3                                             error                   P
    5 + 3 *                                             error                   P
    / 4 - 2                                             error                   P
    8 ^ 2 +                                             error                   P
    
    5 ++ 3                                              error                   P
    8 // 2                                              error                   P
    4 ** 2                                              error                   P
    1 +-+ 2                                             -1                      P

"""
import sys
import operator
opr = {'+':operator.add, '-':operator.sub, '/':operator.truediv, '*':operator.mul, '^':operator.pow}

def find_innermost_parentheses(full_expression: str):
    """Checks if expression contains parentheses. Finds inner most parenthesis pair. Returns index of opening and closing parenthesis."""
    if '(' in full_expression or ')' in full_expression:
        start_index = full_expression.rfind('(')
        for counter in range(start_index+1, len(full_expression)):
            if full_expression[counter] == ')':
                end_index = counter
                return start_index, end_index
    else:
        return 0, len(full_expression)-1

def fix_operators(full_expression: str)->str:
    """Checks if '**','x', 'X', '×','\u2212','÷', and '-+'  are in the string expression. 
    Replaces them with '^', '*', '*', '*' , '-', '/', '-' respectively. Returns updated string."""
    if '**' in full_expression:
        full_expression = full_expression.replace('**','^')
    if 'x' in full_expression:
        full_expression = full_expression.replace('x','*')
    if 'X' in full_expression:
        full_expression = full_expression.replace('X','*')
    if '×' in full_expression:
        full_expression = full_expression.replace('×','*')
    if '\u2212' in full_expression:
        full_expression = full_expression.replace('\u2212','-')
    if '÷' in full_expression:
        full_expression = full_expression.replace('÷','/')
    return full_expression

def consolidate_signs(expression: str)-> str:
    """Replaces all instances of ++, --, +-, and -+ with +, +, -, and - respectively."""
    if '++' in expression:
        expression = expression.replace('++','+')
    if '--' in expression:
        expression = expression.replace('--','+')
    if '+-' in expression:
        expression = expression.replace('+-','-')
    if '-+' in expression:
        expression = expression.replace('-+','-')
    return expression

def check_prime_operator(full_expression: str):
    """Checks string expression for presence of operator. Returns the prime operator."""
    if '^' in full_expression:
            return '^'
    if '*' in full_expression:   
        return '*'
    if '/' in full_expression:
        return '/'
    if '+' in full_expression: 
        return '+'
    if '-' in full_expression:
        if full_expression[0] == '(':
            if full_expression.find('-') == 1 and full_expression.count('-') == 1:
                return True
            else:
                return '-'
        elif full_expression.find('-') == 0 and full_expression.count('-') == 1:
                return False
        else:  
            return '-'
    elif any(operator in full_expression for operator in ('(',')')):
            return True      
    else:
        return False 
    
def find_prime_operator(full_expression: str, prime_operator: str):
    """Finds prime_operator in full_expression, returns it's index."""
    return full_expression.find(prime_operator), prime_operator
 
def find_operation_index(full_expression: str, operator_index: int)->int:
    """Finds index of last digit before and after operator, ie start and end index of operation.
    Returns the start and end indexes."""
    start_index = 0
    end_index = 0
    if operator_index != 0:
        n = -1
        while operator_index+n >= 0 and full_expression[operator_index+n].isdigit() or operator_index+n >= 0 and full_expression[operator_index+n] == '.' or operator_index+n >= 0 and full_expression[operator_index+n] == '-':  
            n -= 1
            if full_expression[operator_index+n+1] == '-':
                break 
        start_index = operator_index+n+1
        n = 1
        while operator_index+n < len(full_expression) and full_expression[operator_index+n].isdigit() or operator_index+n < len(full_expression) and full_expression[operator_index+n] == '.' or operator_index+n < len(full_expression) and full_expression[operator_index+n] == '-' and n == 1:
            n += 1
        end_index = operator_index+n-1
        
    elif operator_index == 0 and full_expression[operator_index] == '-':
        start_index == operator_index
        n = 1
        while operator_index+n < len(full_expression) and full_expression[operator_index+n].isdigit() or operator_index+n < len(full_expression) and full_expression[operator_index+n] == '.' or operator_index+n < len(full_expression) and full_expression[operator_index+n] == '-' and n == 2:
            n += 1
        end_index = operator_index+n-1
    return start_index, end_index

def take_operation(full_expression: str, start_index: int, end_index: int)-> str:
    """Takes string expression from a larger expression given the index values of what to take. 
    Creates a new string composed of the string expression taken.  
    Returns the new string.  """
    operation = ''
    if start_index == 0 and end_index == len(full_expression)-1:
        return full_expression
    else:
        for index in range(start_index, end_index+1):
            operation += full_expression[index]
        return operation

def operation_to_n(full_expression: str, start_index: int, end_index:int)-> list[str]:
    """Replaces string operation with n. Start and end of operation referred to by start and end index arguments. """
    full_expression_n = []
    for index, element in enumerate(full_expression):
        if index in range(start_index, end_index+1):
            full_expression_n.append('n')
        else:
            full_expression_n.append(element)
    return full_expression_n

def calculate_str_operation(str_operation: str, prime_operator: str)-> float:
    """Calculates string expression of two operands.
    Calls find_index_prime_operator. Splits string using operator. Converts list of string operands into floats, and calculates
    expression using operator using opr dictionary. Returns float."""
    operands = str_operation.split(prime_operator)
    if operands[0] == '':
        operands[1] = '-' + operands[1]
        operands[2] = '-' + operands[2]
        operands.remove('')
        prime_operator = '+'
    return opr[prime_operator](float(operands[0]), float(operands[1]))

def update_expression(full_expression: str, start_index: int, end_index:int, operation_result: float)->str:
    """ Calls operation_to_n. Checks value before and after n group. If parenthesis, does nothing.
    If number, replaces the n adjacent with multiplication operator. If operator, does nothing.
    Replaces the n group with str result of expression of two operands.
    
    Conditions for determining when to add * and when to add + to leading or trailing n:
        If the str_expression taken contained parenthesis, if any n of n group adjacent to digit, replace that n 
        with '*'.
        
        If the str_expression taken did not contain parentheses, if any n of n group adjacent to digit, replace
        that n with '+'.
        """

    #Replace taken operation with n
    full_expression_n = operation_to_n(full_expression, start_index, end_index)
    # Check if element before and after n group is a number. If number, replace adjacent n with multiplication operator.
    if full_expression[start_index] == ('('):
        if full_expression_n.index('n') != 0:
            if full_expression_n[full_expression_n.index('n')-1].isdigit():
                full_expression_n[full_expression_n.index('n')] = '*'
        if full_expression_n.index('n')+full_expression_n.count('n') < len(full_expression_n):
            if full_expression_n[full_expression_n.index('n')+full_expression_n.count('n')].isdigit():
                full_expression_n[full_expression_n.index('n')+full_expression_n.count('n')-1] = '*' 
    elif full_expression[start_index] != ('('):
        if full_expression_n.index('n') != 0:
            if full_expression_n[full_expression_n.index('n')-1].isdigit():
                full_expression_n[full_expression_n.index('n')] = '+'
        if full_expression_n.index('n')+full_expression_n.count('n') < len(full_expression_n):
            if full_expression_n[full_expression_n.index('n')+full_expression_n.count('n')].isdigit():
                full_expression_n[full_expression_n.index('n')+full_expression_n.count('n')-1] = '+'
    #Replace n group with operation result and return updated string 
    operation_result = str(operation_result)
   
    #Remove 'n' group, except for last.
    for iteration in range(full_expression_n.count('n')-1):
        full_expression_n.remove('n')
    
    #Replace last 'n' with str operation result
    full_expression_n[full_expression_n.index('n')] = operation_result
    updated_str_expression = ''
    for element in full_expression_n:
        updated_str_expression += element
    return updated_str_expression

def calculate(full_expression: str):
    """Calls find_prime_operator, find_operation_index, take_operation, update_full_expression, calculate_str_operation"""
    operation_result = 0
    #In this context, operation refers to two operands and an operator. Expression refers to multiple operations.
    while check_prime_operator(full_expression):        
        expression_index = find_innermost_parentheses(full_expression)
        str_expression = take_operation(full_expression, expression_index[0], expression_index[1]) 
        if check_prime_operator(str_expression) == True:
                operation_result = str_expression.strip('()')  
        else: 
            while check_prime_operator(str_expression):
                prime_operator = find_prime_operator(str_expression, check_prime_operator(str_expression))
                operation_index = find_operation_index(str_expression, prime_operator[0])
                str_operation = take_operation(str_expression, operation_index[0], operation_index[1])
                operation_result = calculate_str_operation(str_operation, prime_operator[1])
                str_expression = update_expression(str_expression, operation_index[0], operation_index[1], operation_result)
                if check_prime_operator(str_expression) == True:
                    break
        full_expression = update_expression(full_expression, expression_index[0], expression_index[1], operation_result)
    return float(full_expression)

def remove_spaces(full_expression: str)-> str:
    expression_list = full_expression.split()
    expression_nospace = ''
    for element in expression_list:
        expression_nospace += element
    return expression_nospace

def remove_operands(expression: str)-> list[float]:
    operand_list = []
    for value in expression:
        if value == '+' or value == '-' or value == '/' or value == '*' or value == 'X' or value == 'x' or value =='^' or value =='(' or value == ')':
            pass
        else:
            operand_list.append(value)
    return operand_list 

def create_string(element_list: list[str])->str:
    """Creates one string from a list of strings via concatenation"""
    new_string = ''
    for element in element_list:
        new_string += element
    return new_string

def check_numbers_operators(expression: str)->bool:
    """Returns True if string containts only numbers and operators."""
    if expression.isdigit():
        print("Expression contains no operators")
        print("Expressions should contain numbers and operators")
        return False
    n = 0
    for element in expression:
        if element.isdigit() == False:
            if any(item in element for item in ('+','-','*','^','/','(',')')) != True:
                print("Expressions should contain only numbers and operators")
                return False
            else:
                n += 1  #Number of operators in expression
    if n == len(expression):
        print("Expression contains no numbers")
        print("Expressions should contain numbers and operators")
        return False
    elif n == 1 and expression[0] == '-':
        print("Expression contains no operations")
        return False
    return True

def invalid_operators(expression: str)->bool:
    """Checks for syntax erros in operators"""
    if any(item in expression[0] for item in ('+','*','^','/',')')):       #Checks if expressions starts with invalid operator
        print("Syntax error")
        return True
    elif any(item in expression[len(expression)-1] for item in ('+','-','*','^','/','(')):  #Checks if expression ends with invalid operator
        print("Syntax error")
        return True
    elif any(item in expression for item in ('^^','//','+*','*+','^+','+^','^*','*^','^/','/^','/*','*/','+/','/+','-/','-^')):
        print("Syntax error")
        return True
    else:
        return False
    
def guard_division_zero(expression: str):
    "Checks if division by zero is present in expression. If present, returns error."
    search_start = 0
    SEARCH_END = len(expression)-1
    
    while expression.find('/',search_start, SEARCH_END) != -1:
        number = ''
        n = 1
        while expression[expression.find('/', search_start, SEARCH_END) + n].isdigit() or any(operator in expression[expression.find('/', search_start, SEARCH_END) + n] for operator in('.','(','-')):
            if expression[expression.find('/', search_start, SEARCH_END) + n] == '(':
                n += 1
                while expression[expression.find('/', search_start, SEARCH_END) + n].isdigit() or any(operator in expression[expression.find('/', search_start, SEARCH_END) + n] for operator in('.','(','-','+','*','^',')')):
                    if expression[expression.find('/', search_start, SEARCH_END) + n] == ')':
                        if calculate(take_operation(expression,expression.find('/', search_start, SEARCH_END) + 1, expression.find('/', search_start, SEARCH_END) + n )) == 0:
                            print("ERROR: Division by zero")
                            return True
                        else:
                            return False 
                    if n + expression.find('/', search_start, SEARCH_END) == SEARCH_END:
                        break
                    n += 1
            if expression[expression.find('/', search_start, SEARCH_END) + n].isdigit():
                number += expression[expression.find('/', search_start, SEARCH_END) + n]
            n += 1
            if n + expression.find('/', search_start, SEARCH_END) == len(expression):
                break
                                            
        if all(char == '0' for char in number):
            print("ERROR: Division by zero")
            return True
        search_start = expression.find('/', search_start, SEARCH_END)+1
    return False

def check_parentheses(expression: str):
    if '(' in expression or ')' in expression:
        if expression.count('(') != expression.count(')'):
            print("ERROR: Unclosed parentheses")
            return True
    else:
        return False


expression = True
print("Calculator ON")
print("Type STOP to end")
print("Supports summation, subtracion, multiplication, divison, and exponentiation")
while expression:
    expression = input()    
    if expression == 'STOP':
        sys.exit()
    else:
#Check if expression has spaces. Remove them with remove_spaces function.
        if ' ' in expression:
            expression = remove_spaces(expression)
#Standardize and simplify operators. 
        expression = fix_operators(expression)
        expression = consolidate_signs(expression)
#Check if expression contains only numbers and operators, and any syntax errors
        while invalid_operators(expression) or check_numbers_operators(expression) is False or guard_division_zero(expression) or check_parentheses(expression):
            expression = input() 
            if expression == 'STOP':
                sys.exit()      
            if ' ' in expression:
                expression = remove_spaces(expression)
            expression = fix_operators(expression)
            expression = consolidate_signs(expression)
#Check if expression is mathematically correct, or makes sense, or syntactically correct... 

#Print Result 
    print(calculate(expression)) 








"""
import operator

['__abs__', '__add__', '__all__', '__and__', '__builtins__', '__cached__', '__call__', '__concat__', '__contains__', '__delitem__', '__doc__', '__eq__', '__file__', '__floordiv__', '__ge__', '__getitem__', '__gt__', '__iadd__', '__iand__', '__iconcat__', '__ifloordiv__', '__ilshift__', '__imatmul__', '__imod__', '__imul__', '__index__', '__inv__', '__invert__', '__ior__', '__ipow__', '__irshift__', '__isub__', '__itruediv__', '__ixor__', '__le__', '__loader__', '__lshift__', '__lt__', '__matmul__', '__mod__', '__mul__', '__name__', '__ne__', '__neg__', '__not__', '__or__', 
'__package__', '__pos__', '__pow__', '__rshift__', '__setitem__', '__spec__', '__sub__', '__truediv__', '__xor__', '_abs', 'abs', 'add', 'and_', 
'attrgetter', 'call', 'concat', 'contains', 'countOf', 'delitem', 'eq', 'floordiv', 'ge', 'getitem', 'gt', 'iadd', 'iand', 'iconcat', 'ifloordiv', 'ilshift', 'imatmul', 'imod', 'imul', 'index', 'indexOf', 'inv', 'invert', 'ior', 'ipow', 'irshift', 'is_', 'is_not', 'isub', 'itemgetter', 'itruediv', 'ixor', 'le', 'length_hint', 'lshift', 'lt', 'matmul', 'methodcaller', 'mod', 'mul', 'ne', 'neg', 'not_', 'or_', 'pos', 'pow', 'rshift', 'setitem', 'sub', 'truediv', 'truth', 'xor']
    """