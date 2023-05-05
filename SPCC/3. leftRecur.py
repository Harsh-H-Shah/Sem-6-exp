input_grammar = '''S -> S + T | T
T -> T * F | F
F -> ( S ) | id
'''

productions = input_grammar.split('\n')

non_terminals = []
for production in productions:
    non_terminal = production.split('->')[0].strip()
    if non_terminal not in non_terminals:
        non_terminals.append(non_terminal)

for A in non_terminals:
    A_productions = [
        production for production in productions if production.startswith(A + ' ->')]

    # Check for left recursion
    has_left_recursion = False
    for production in A_productions:
        if production.split('->')[1].strip().startswith(A):
            has_left_recursion = True
            break

    # Remove left recursion
    if has_left_recursion:
        A_prime = A + "'"
        productions.append(A_prime + ' -> ' + A_prime + ' ' + '|'.join([production.split('->')[1].strip()[
                           1:] + ' ' + A_prime for production in A_productions if production.split('->')[1].strip().startswith(A)]))
        productions.append(A + ' -> ' + '|'.join([production.split('->')[1].strip() + ' ' + A_prime + ' | ' + production.split(
            '->')[1].strip() for production in A_productions if not production.split('->')[1].strip().startswith(A)]))
        productions.remove(
            A + ' -> ' + '|'.join([production.split('->')[1].strip() for production in A_productions]))

output_grammar = '\n'.join(productions)
print(output_grammar)
