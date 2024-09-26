def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    if operator == '+':
        values.append(left + right)
    elif operator == '-':
        values.append(left - right)
    elif operator == '*':
        values.append(left * right)
    elif operator == '/':
        values.append(left / right)

def dynamic_calculator(expression):
    operators = []  
    values = []     
    i = 0
    
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        elif expression[i].isdigit(): 
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            values.append(num)
            continue
        elif expression[i] == '(':
            operators.append('(')
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()  
        elif expression[i] in '+-*/':
            while (operators and operators[-1] != '(' and
                   (operators[-1] in '*/' or expression[i] in '+-')):
                apply_operator(operators, values)
            operators.append(expression[i])
        i += 1
    
    while operators:
        apply_operator(operators, values)
    
    return values[0]

expression = input("Enter a mathematical expression: ")
result = dynamic_calculator(expression)
print(f"Result: {result}")
