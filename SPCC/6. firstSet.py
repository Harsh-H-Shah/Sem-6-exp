input_grammar = '''S -> AB | BC | a
A -> BA | a
B -> CC | b
C -> AB | a | epsilon
'''

productions = input_grammar.split('\n')

first_sets = {}

for production in productions:
    non_terminal, derivation = production.split('->')
    non_terminal = non_terminal.strip()
    derivation = derivation.strip()

    if non_terminal not in first_sets:
        first_sets[non_terminal] = set()

    if derivation[0].islower():
        first_sets[non_terminal].add(derivation[0])

    elif derivation[0].isupper():
        first_sets[non_terminal].update(first_sets[derivation[0]])

        i = 0
        while 'epsilon' in first_sets[derivation[i]]:
            i += 1
            if i == len(derivation):
                first_sets[non_terminal].add('epsilon')
                break
            first_sets[non_terminal].update(first_sets[derivation[i]])

for non_terminal in first_sets:
    print(
        f"FIRST({non_terminal}) = {{{', '.join(sorted(list(first_sets[non_terminal])))}}}")
