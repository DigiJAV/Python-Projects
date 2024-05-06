"""
Tests:
((7.2^3 + 9.81/2.5) * (4.6^2 - 3.14)) / (((5.7^2 * 1.618) - (2.718^1.5)) + ((6.28/3.14) * 1.414)) - (((9.8 * 6.67) ^ 0.333) / (2.0 ^ (4.0/3.0))) + (((3.3 * 2.4) ^ 1.2) * (1.5 / 0.75) * (1.0 - (1.0/3.0)))  
    result: 147.86518934854774

3/2*0       Result: 0

((3.1416 ^ 2.7183) * ((22.0 / 7.0) ^ 1.618)) + (((0.5772 * 2.7183) ^ 3.1416) - (1.6180 ^ (9.8696 / 3.1416))) / ((6.6743 ^ (1.0 / 3.0)) * (1.4142 * (8.0 ^ (1.0 / 3.0)))) - (((2.7183 ^ (6.6743 / 6.0285)) * (3.1416 ^ 2.7183)) / ((6.0285 ^ 1.6180) * (1.6180 ^ 6.6743))) + (((4.6692 * 1.6180) ^ 2.7183) - ((0.5772 ^ 3.1416) * (6.6743 / 1.4142)))
    result: 386.1080049426594
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
    if '/' in full_expression:
        return '/'
    if '*' in full_expression:   
        return '*'
    if '+' in full_expression: 
        return '+'
    if '-' in full_expression:
        if full_expression[0] == '(':
            if full_expression.find('-') == 1 and full_expression.count('-') == 1:
                return True     #Example expression for when this applies: (-12). Return True will result, further in the program, in the expression having its parentheses removed , since there are no more operations to be made. This will enable to it to be converted to a float and printed for user. 
            else:
                return '-'
        elif full_expression.find('-') == 0 and full_expression.count('-') == 1:        ##
            if any(element in full_expression for element in ('(',')')):                ##
                return True                                                             ##
            else:                                                                       ##
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
 
def find_operation_index(expression: str, operator_index: int)->int:
    """Finds index of last digit before and after operator, ie start and end index of operation.
    Returns the start and end indexes."""
    start_index = 0
    end_index = 0
    operand_index = operator_index + n
    value = expression[operand_index]
    iterator_sign: int 
    n: int
    check_side = 'left'
    early_break = False

    if operator_index != 0:
        while check_side:
            if check_side == 'left':
                iterator_sign = -1
                n = iterator_sign
            elif check_side == 'right':
                iterator_sign = 1
                n = iterator_sign
            while value.isdigit() or value is any(element in value for element in ('.','-','+','e')):
                if value == '+' and expression[operand_index-1] != 'e':
                    if check_side == 'left':
                        n += 1
                        start_index = operand_index
                        check_side = 'right'
                        early_break = True
                        break
                    elif check_side == 'right':
                        n -= 1
                        end_index = operand_index
                        check_side == 0
                        early_break = True
                        break 
                if value == '-' and expression[operand_index-1] != 'e':
                    if check_side == 'left':
                        start_index = operand_index
                        check_side = 'right'
                        early_break = True
                        break
                    elif check_side == 'right':
                        n -= 1
                        end_index = operand_index
                        check_side == 0
                        early_break = True
                        break 
                if operand_index == 0:
                    start_index = operand_index
                    check_side = 'right'
                    early_break = True
                    break
                elif operand_index == len(expression) - 1:
                    end_index = operand_index
                    check_side == 0
                    early_break = True
                    break 
                n += iterator_sign
            if early_break != True:
                if check_side == 'left':
                    n += 1
                    start_index = operand_index
                    check_side = 'right'
                elif check_side == 'right':
                    n -= 1
                    end_index = operand_index
                    check_side = 0
                    
    elif operator_index == 0:
        start_index = operand_index 
        check_side = 'right'
        n = 1
        while value.isdigit() or any(element in value for element in ('.','-')) or operand_index < len(expression)-1:
            if expression.count('-', operator_index, operand_index) == 3:
                n -= 1
                break
            n += 1 
        end_index = operand_index

    return start_index, end_index    

                        
    """ Old code 
    #If the operator is not at index 0 of the expression, check values before it. The only operator that can validly be at this index is the subtraction operator.
    if operator_index != 0:
        n = -1
        while operator_index+n >= 0 and full_expression[operator_index+n].isdigit() or operator_index+n >= 0 and any(element in full_expression[operator_index+n] for element in ('.','-','+')):  
            ########################
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
    """
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
    """Removes spaces from string math expression given by user."""
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
            if any(item in element for item in ('+','-','*','^','/','(',')','.')) != True:
                print("Expressions should contain only numbers and operators")
                return False
            elif element != '.':
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
    elif any(item in expression for item in ('^^','//','+*','*+','^+','+^','^*','*^','^/','/^','/*','*/','+/','/+','-/','-^')):  #Checks for invalid operation combinations
        print("Syntax error")
        return True
    else:
        return False
    
def guard_division_zero(expression: str):
    "Checks if division by zero is present in expression. If present, returns error."
    #First search for division operator covers whole expression. 
    search_start = 0
    SEARCH_END = len(expression)-1
    #Index of parentheses under which is the denominator to be checked
    parentheses_index = expression.find('/', search_start, SEARCH_END)                                
    #While there exists a parenthesis operator within the check interval.
    while parentheses_index != -1:   
        #Index iterator
        n = 1   
        #Index of value in the denominator being checked
        check_index = parentheses_index + n    
        #Element in expression at check index
        value = expression[check_index] 
        #String which contains digits composing the denominator. Used when there are no operations under the denominator.
        number = '' 
        #Boolean used to skip checking of number string. Becomes true when it is known that the string has a nonzero value. 
        stop_check = False 
        #Boolean used to break from secondary while loop to the primary; applies when a denominator containing operation(s) does not trigger division by zero error. 
        denominator_break = False                                          
        #If the checked value is any of the following, continue loop: a digit, a period, an opening parenthesis, or a minus operator. If there is no expression or operation (contained by parenthesis) that falls under the division operator, and  
        while value.isdigit() or any(operator in value for operator in('.','(','-')):   
            if n > 1 and value == '-': #if expression at any n > 1 is '-', stop loop
                break
            if n > 2 and value == '(': #If expression at any n > 2 is '(', stop loop 
                break 
            ##BRANCH OFF, LOOP THROUGH EXPRESSION 
            #If checked value is an opening parenthesis, branch off to check expression contained in the parentheses.    
            if value == '(': 
                stop_check = True
                #Initialize  open and close parentheses counters
                open_parenthesis_counter = 1     
                close_parenthesis_counter = 0   
                # Move on to next element in the expression by adding 1 to check index value
                n += 1  
                check_index = parentheses_index + n 
                value = expression[check_index]
                #If checked value is a digit, any operator, a period, or a parenthesis, continue loop. 
                while value.isdigit() or any(operator in value for operator in('.','(','-','+','*','^','/',')')):
                    if value == '(':
                        open_parenthesis_counter += 1
                    if value == ')':  
                        close_parenthesis_counter += 1
                    #If end of expresion reached, signified by equal amount of close and open parenthesis.
                    if open_parenthesis_counter == close_parenthesis_counter:
                        #Take the expression corresponding to the outermost parentheses. This is the denominator of the selected division operator.  
                        denominator_expression = take_operation(expression, parentheses_index + 1, check_index)
                        #If there is another division operator in the denominator expression, run guard_division_zero on that expression
                        if denominator_expression.find('/', parentheses_index + 1, check_index) != -1:
                            if guard_division_zero(denominator_expression):
                                return True
                        #If there are no division operators in the expression, or division operators do not trigger error, calculate the result. If zero, return error.
                        if calculate(take_operation(expression, parentheses_index + 1, check_index )) == 0:
                            #If result of expression is zero, print division by zero error.
                            print("ERROR: Division by zero")         
                            return True
                        #If denominator expression result is not zero, break and continue search at final check_index value. 
                        else:
                            denominator_break = True
                            break 
                    #Move to next element in expression
                    n += 1 
                    check_index = parentheses_index + n 
                    value = expression[check_index]

            #True when result of operation containing denominator is not zero. Breaks to main loop, to start search for next division operator.
            if denominator_break:
                break
            ##If there is no opening parenthesis, this means there is no expression or operation after the selected division operator.
            #Break as soon as a non zero digit encnountered, since denominator is not zero.        
            else:
                if value.isdigit():     
                    if value != '0':
                        stop_check = True
                        break                            #Break at the first encounter with a non-zero digit, since this means the denominator is nonzero. 
                    number += value    #Concatenate the digit to number string variable.  
                #Move to next element in expression
                n += 1  
                check_index = parentheses_index + n     
                value = expression[check_index]
                if check_index == len(expression):
                    break       
        if stop_check == False:
            if all(char == '0' for char in number):
                print("ERROR: Division by zero")
                return True
        #Start next search at check index. If the denominator was an expression with operator, this will necessarily be at the last element in the expression. If it did not contain other operations, check_will be where first non-zero digit encountered. 
        search_start = check_index
        parentheses_index = expression.find('/', search_start, SEARCH_END)
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
    print("Result: ", calculate(expression)) 



