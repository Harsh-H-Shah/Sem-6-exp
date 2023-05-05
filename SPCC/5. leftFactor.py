input_grammar = '''S -> AB | AC | AD | AE
A -> a | aB
B -> bC | bD | bE
C -> c
D -> d
E -> e | epsilon
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

    prefix = ''
    for i in range(len(A_productions[0].split('->')[1])):
        if all([production.split('->')[1][i] == A_productions[0].split('->')[1][i] for production in A_productions]):
            prefix += A_productions[0].split('->')[1][i]
        else:
            break

    if prefix != '':
        A_prime = A + "'"
        new_productions = []
        new_productions.append(A + ' -> ' + prefix + A_prime)
        for production in A_productions:
            if production.split('->')[1].startswith(prefix):
                new_productions.append(
                    A_prime + ' -> ' + production.split('->')[1][len(prefix):] + ' | epsilon')
            else:
                new_productions.append(A + ' -> ' + production.split('->')[1])
        productions.remove('\n'.join(A_productions))
        productions.extend(new_productions)

output_grammar = '\n'.join(productions)
print(output_grammar)
