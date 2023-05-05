input_grammar = '''S -> A
A -> aB | epsilon
B -> bA | c
'''

follow_sets = {}

for production in input_grammar.split('\n'):
    non_terminal, derivation = production.split('->')
    non_terminal = non_terminal.strip()
    derivation = derivation.strip()

    if non_terminal not in follow_sets:
        follow_sets[non_terminal] = set()

    i = 0
    while i < len(derivation):
        symbol = derivation[i]

        if symbol.isupper():
            if i == len(derivation) - 1:
                follow_sets[symbol].update(follow_sets[non_terminal])
            else:
                j = i + 1
                while j < len(derivation):
                    if derivation[j].islower():
                        follow_sets[symbol].add(derivation[j])
                        break
                    elif derivation[j].isupper():
                        if j == len(derivation) - 1:
                            follow_sets[symbol].update(
                                follow_sets[non_terminal])
                        else:
                            k = j + 1
                            while k < len(derivation):
                                if derivation[k].islower():
                                    follow_sets[symbol].add(derivation[k])
                                    break
                                elif derivation[k].isupper():
                                    if 'epsilon' not in follow_sets[derivation[k]]:
                                        follow_sets[symbol].update(
                                            follow_sets[derivation[k]])
                                        break
                                    else:
                                        follow_sets[symbol].update(
                                            follow_sets[derivation[k]].difference({'epsilon'}))
                                k += 1
                            else:
                                follow_sets[symbol].update(
                                    follow_sets[non_terminal])
                    j += 1

        i += 1

# Output the FOLLOW sets
for non_terminal in follow_sets:
    print(
        f"FOLLOW({non_terminal}) = {{{', '.join(sorted(list(follow_sets[non_terminal])))}}}")
