"""
Tests:
p = test passed
f = test failed

((7.2^3 + 9.81/2.5) * (4.6^2 - 3.14)) / (((5.7^2 * 1.618) - (2.718^1.5)) + ((6.28/3.14) * 1.414)) - (((9.8 * 6.67) ^ 0.333) / (2.0 ^ (4.0/3.0))) + (((3.3 * 2.4) ^ 1.2) * (1.5 / 0.75) * (1.0 - (1.0/3.0)))  
    result: 147.86518934854774
    p

3/2*0       Result: 0
    p   

((3.1416 ^ 2.7183) * ((22.0 / 7.0) ^ 1.618)) + (((0.5772 * 2.7183) ^ 3.1416) - (1.6180 ^ (9.8696 / 3.1416))) / ((6.6743 ^ (1.0 / 3.0)) * (1.4142 * (8.0 ^ (1.0 / 3.0)))) - (((2.7183 ^ (6.6743 / 6.0285)) * (3.1416 ^ 2.7183)) / ((6.0285 ^ 1.6180) * (1.6180 ^ 6.6743))) + (((4.6692 * 1.6180) ^ 2.7183) - ((0.5772 ^ 3.1416) * (6.6743 / 1.4142)))
    result: 386.1080049426594
    p

((5^(2/3) + (17 * 2^4)/9) * (1/2 - 1/6))/(3^(1/2) - (29/15 * 7^(1/3)))
    result: -5.619103510175150293702364854203035757016702056384609271626682005
    p

-3(6)
    result: -18
    p
(1/2-1/6)
    result: 0.3333333333
    p

(((3^5)^(1/4) * (7/12)) / ((23/8) - (1/11))) + ((5^3)^(1/2) * (2/3))
    result: 8.2808064474265799634
    p

((((9^2)^(1/3) - (5/17)) * (3/8))^2 + (7^(1/2) * (1/5))) / ((41/16)^(1/4) - (11/6 * (2/3)^5))
    result: 2.7505653165650875333
    p

((((15^3)^(1/4) + (1/9)^4) * ((5/2)^2 - 4/19)) / (((17/7)^3 - (1/13)^6)^(1/2))) + (((3^5)^(1/3) * (11/20)) / (7^(1/2) - (23/14)))
    result: 15.5854913462201659229261
    p

(((((7^4)^(1/5) * (3/8)) - ((29/11)^2 + (1/7)^7)) * (((2/3)^5 + (5/2)^3)^(1/4))) / ((((19/6)^4 - (1/15)^8)^(1/3)) + ((11^2)^(1/2) * (7/12))))
    result: -0.9310531023184527
    p

((((((5^6)^(1/6) + (1/11)^9) * ((17/4)^3 - (3/16)^11)) - (((7^5)^(1/5) * (13/18)) + ((31/8)^2 + (1/9)^12))) * ((((3/2)^7 + (11/3)^4)^(1/5)) - ((23^2)^(1/3) * (5/14)))) / (((((17/6)^5 - (1/17)^13)^(1/4)) + ((19^3)^(1/4) * (7/10))) - ((((3^7)^(1/6) * (11/16)) - ((29/5)^2 + (1/11)^14)) * (((5/3)^8 + (13/2)^5)^(1/6)))))
    result: -0.021313312662757024
    p

(((((((9^7)^(1/7) + (1/13)^15) * ((23/5)^4 - (5/22)^17)) - ((((11^6)^(1/6) * (17/21)) + ((37/9)^3 + (1/11)^18))* (((7/3)^9 + (15/2)^6)^(1/7)))) * (((((5/2)^11 + (19/4)^7)^(1/8)) - ((31^3)^(1/4) * (9/20))))) / ((((((23/7 )^6 - (1/19)^19)^(1/5)) + ((27^4)^(1/5) * (11/14))) - (((((7^8)^(1/7) * (15/22)) - ((41/7)^3 + (1/13) ^20)) * (((9/4)^12 + (17/3)^7)^(1/8)))))) + (((((13^5)^(1/6) * (3/10)) / ((5^4)^(1 /5) - (47/13))) + ((((2/3)^13 + (19/5)^8)^(1/9)) * (7^3)^(1/6))) * ((23^2)^(1/4) * (11/18)))))
    result: 893.7768766741522
    p

((((((((15^8)^(1/8) + (1/15)^21) * ((29/6)^5 - (7/28)^23)) - (((((17^7)^(1/7) * (21/25)) + ((49/11)^4 + (1/13)^24)) * (((11/4)^13 + (21/3)^8)^(1/9))))) * ((((((9/3)^15 + (23/5)^9)^(1/10)) - ((39^4)^(1/5) * (13/24)))))) / (((((((31/8)^7 - (1/21)^25)^(1/6)) + ((35^5)^(1/6) * (15/18))) - ((((((11^9)^(1/8) * (19/26)) - ((53/9)^4 + (1/15)^26)) * (((13/5)^16 + (25/4)^9)^(1/10)))))))+ ((((((17^6)^(1/7) * (5/12)) / ((7^5)^(1/6) - (59/15))) + (((((4/5)^17 + (27/6)^10)^(1/11)) * (11^4)^(1/7))))) * ((31^3)^(1/5) * (15/22))))))
    result: ?
    output: ERROR: Unclosed parentheses
        number of opening parenthesis != closing parenthesis
    p

(((((((((23^9)^(1/9) + (1/17)^27) * ((37/7)^6 - (9/34)^29)) - ((((((23^8)^(1/8) * (27/29)) + ((61/13)^5 + (1/15)^30)) * (((15/5)^17 + (29/4)^10)^(1/11)))))) * (((((((13/4)^19 + (31/6)^11)^(1/12)) - ((47^5)^(1/6) * (17/28)))))))/ ((((((((39/9)^8 - (1/23)^31)^(1/7)) + ((43^6)^(1/7) * (19/22))) - (((((((15^10)^(1/9) * (23/30)) - ((67/11)^5 + (1/17)^32)) * (((17/6)^20 + (33/5)^11)^(1/12))))))))+ (((((((21^7)^(1/8) * (7/14)) / ((9^6)^(1/7) - (71/17))) + ((((((6/7)^21 + (35/7)^12)^(1/13)) * (15^5)^(1/8)))))) * ((39^4)^(1/6) * (19/26)))))))) + ((((5^11)^(1/10) * (3/8)) + (((((2/3)^22 + (11/2)^13)^(1/14)) * (7^6)^(1/9))) * ((3^7)^(1/8) * (23/30))))            
    result: ?
    output: ERROR: Unclosed parentheses
        # opening parenthesis != closing parenthesis
    p
"""

import sys
import operator
import os
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
    return full_expression.find(prime_operator)
 
def find_operation_index(expression: str, operator_index: int)->int:
    """Finds index of last digit before and after operator, ie start and end index of operation.
    Returns the start and end indexes."""
    start_index = 0
    end_index = 0
    check_side = 'left'
    if operator_index != 0:
        while check_side:
            early_break = False
            if check_side == 'left':
                iterator_sign = -1
            elif check_side == 'right':
                iterator_sign = 1
            n = iterator_sign
            operand_index = operator_index + n
            value = expression[operand_index]
            while value.isdigit() or any(element in value for element in ('.','-','+','e')):
                if check_side == 'left':
                    if value == '+':
                        n += 1
                        operand_index = operator_index + n
                        start_index = operand_index
                        check_side = 'right'
                        early_break = True
                        break
                    elif value == '-':
                        start_index = operand_index
                        check_side = 'right'
                        early_break = True
                        break
                    elif operand_index == 0:                  
                        start_index = operand_index
                        check_side = 'right'
                        early_break = True
                        break
                if check_side == 'right':
                    if value == '+':
                        n -= 1
                        operand_index = operator_index + n
                        end_index = operand_index
                        check_side = 0
                        early_break = True
                        break
                    elif value == '-' and operand_index != operator_index+1 :
                        n -= 1
                        operand_index = operator_index + n
                        end_index = operand_index
                        check_side = 0
                        early_break = True
                        break
                    elif operand_index == len(expression) - 1:  
                        end_index = operand_index
                        check_side = 0
                        early_break = True
                        break 
                n += iterator_sign
                operand_index = operator_index + n
                value = expression[operand_index]
            if early_break != True:
                if check_side == 'left':
                    n += 1
                    operand_index = operator_index + n
                    start_index = operand_index
                    check_side = 'right'
                elif check_side == 'right':
                    n -= 1
                    operand_index = operator_index + n
                    end_index = operand_index
                    check_side = 0 
    elif operator_index == 0:
        start_index = operator_index
        check_side = 'right'
        n = 1
        operand_index = operator_index + n
        value = expression[operand_index]
        while value.isdigit() or any(element in value for element in ('.','-')) or operand_index < len(expression)-1:
            if expression.count('-', operator_index, operand_index) == 3:
                n -= 1
                break
            n += 1 
        operand_index = operator_index + n
        end_index = operand_index

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
                prime_operator = check_prime_operator(str_expression)
                prime_operator_index = find_prime_operator(str_expression, prime_operator)
                operation_index = find_operation_index(str_expression, prime_operator_index)
                str_operation = take_operation(str_expression, operation_index[0], operation_index[1])
                operation_result = calculate_str_operation(str_operation, prime_operator)
                operation_result = scientific_notation_to_float(operation_result)
                str_expression = update_expression(str_expression, operation_index[0], operation_index[1], operation_result)
                if check_prime_operator(str_expression) == True:
                    break
        full_expression = update_expression(full_expression, expression_index[0], expression_index[1], operation_result)
        full_expression = consolidate_signs(full_expression)
        print(full_expression)
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
    #The first search for a division operator covers whole expression. 
    search_start = 0
    SEARCH_END = len(expression)-1
    #Index of parentheses under which is the denominator to be checked
    division_operator_index = expression.find('/', search_start, SEARCH_END)                                
    #While there exists a division operator within the check interval, loop continues. 
    while division_operator_index != -1:   
        #Index iterator
        n = 1   
        #Index of value in the denominator being checked
        check_index = division_operator_index + n    
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
                check_index = division_operator_index + n 
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
                        denominator_expression = take_operation(expression, division_operator_index + 1, check_index)
                        #If there is another division operator in the denominator expression, run guard_division_zero on that expression
                        if denominator_expression.find('/', division_operator_index + 1, check_index) != -1:
                            if guard_division_zero(denominator_expression):
                                return True
                        #If there are no division operators in the expression, or division operators do not trigger error, calculate the result. If zero, return error.
                        if calculate(denominator_expression) == 0:
                            #If result of expression is zero, print division by zero error.
                            print("ERROR: Division by zero")         
                            return True
                        #If denominator expression result is not zero, break and continue search at final check_index value. 
                        else:
                            denominator_break = True
                            break 
                    #Move to next element in expression
                    n += 1 
                    check_index = division_operator_index + n 
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
                check_index = division_operator_index + n     
                value = expression[check_index]
                if check_index == len(expression):
                    break       
        if stop_check == False:
            if all(char == '0' for char in number):
                print("ERROR: Division by zero")
                return True
        #Start next search at check index. If the denominator was an expression with operator, this will necessarily be at the last element in the expression. If it did not contain other operations, check_will be where first non-zero digit encountered. 
        search_start = check_index
        division_operator_index = expression.find('/', search_start, SEARCH_END)
    return False

def scientific_notation_to_float(operation_result):
    """Checks if operation result is in scientific notation. Converts it to a float. Returns the float."""
    if 'e' in str(operation_result):
        operation_result = format(float(operation_result), '.16f')
    return operation_result

def check_parentheses(expression: str):
    if '(' in expression or ')' in expression:
        if expression.count('(') != expression.count(')'):
            print("ERROR: Unclosed parentheses")
            return True
    else:
        return False

def clear_terminal():
    """When called, executes clear terminal command. Determines the operating system to issue the right command."""
    os.system('cls' if os.name == 'nt' else 'clear')

expression = True
print("Calculator ON")
print("Type 'STOP' to end program")
print("Type 'clear' to clear terminal")
print("Supports summation, subtracion, multiplication, divison, and exponentiation")
while expression:
    expression = input()    
    if expression == 'STOP':
        sys.exit()
    elif expression == 'clear':
        clear_terminal()
        print("Calculator ON")
        print("Type 'STOP' to end program")
        print("Type 'clear' to clear terminal")
        print("Supports summation, subtracion, multiplication, divison, and exponentiation")
        continue
    else:
#Check if expression has spaces. Remove them with remove_spaces function.
        if ' ' in expression:
            expression = remove_spaces(expression)
#Standardize and simplify operators. 
        expression = fix_operators(expression)
        expression = consolidate_signs(expression)
#Check if expression contains only numbers and operators, and any syntax errors
        while invalid_operators(expression) or check_numbers_operators(expression) is False or check_parentheses(expression) or guard_division_zero(expression):
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



