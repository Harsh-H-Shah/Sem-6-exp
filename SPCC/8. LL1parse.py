input_grammar = '''S -> E
E -> T E'
E' -> + T E' | epsilon
T -> F T'
T' -> * F T' | epsilon
F -> ( E ) | id
'''

input_first_sets = {
    'S': {'(', 'id'},
    'E': {'(', 'id'},
    "E'": {'+', 'epsilon'},
    'T': {'(', 'id'},
    "T'": {'*', 'epsilon'},
    'F': {'(', 'id'}
}

input_follow_sets = {
    'S': {'$', ')'},
    'E': {'$', ')', '+'},
    "E'": {'$', ')'},
    'T': {'$', ')', '+', '*'},
    "T'": {'$', ')', '+'},
    'F': {'$', ')', '+', '*'}
}

parsing_table = {}

for production in input_grammar.split('\n'):
    non_terminal, derivation = production.split('->')
    non_terminal = non_terminal.strip()
    derivation = derivation.strip()

    for terminal in input_first_sets[non_terminal]:
        if terminal != 'epsilon':
            parsing_table[(non_terminal, terminal)] = production

    if 'epsilon' in input_first_sets[non_terminal]:
        for terminal in input_follow_sets[non_terminal]:
            parsing_table[(non_terminal, terminal)] = production

print(f"{'':<10}", end='')
for terminal in input_follow_sets['S']:
    print(f"{terminal:<10}", end='')
print()

for non_terminal in input_first_sets:
    print(f"{non_terminal:<10}", end='')
    for terminal in input_follow_sets['S']:
        if (non_terminal, terminal) in parsing_table:
            print(f"{parsing_table[(non_terminal, terminal)]:<10}", end='')
        else:
            print(f"{'':<10}", end='')
    print()
