operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
precedence = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def infix_to_tac(expr):
    stack = []
    output = []

    for char in expr:
        if char.isdigit():
            output.append(char)
        elif char in operators:
            while stack and stack[-1] in operators and precedence[char] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    tac = []
    temp_counter = 1
    for token in output:
        if token.isdigit():
            tac.append(f't{temp_counter} = {token}')
            stack.append(f't{temp_counter}')
            temp_counter += 1
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            tac.append(f't{temp_counter} = {operand1} {token} {operand2}')
            stack.append(f't{temp_counter}')
            temp_counter += 1
    print(output)
    return tac


# Direct input and output
expr = input('Enter an infix expression: ')
tac = infix_to_tac(expr)
print('\n'.join(tac))
