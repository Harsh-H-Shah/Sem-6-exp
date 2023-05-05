macro_def_table = {}
macro_inv_table = {}
input_program = input().splitlines()
output_program = []

for line in input_program:
    line = line.split(';')[0]  # Remove comments
    if line.startswith('MACRO'):
        macro_name, params = line.split()[1], line.split()[2:]
        macro_def_table[macro_name] = {'params': params, 'lines': []}
    elif line.startswith('MEND'):
        pass
    elif line.startswith('&'):
        macro_name = line.split()[0][1:]
        arg_values = line.split()[1:]
        macro_inv_table[macro_name] = arg_values
        macro_def = macro_def_table[macro_name]
        macro_lines = macro_def['lines']
        for macro_line in macro_lines:
            for i, arg_name in enumerate(macro_def['params']):
                macro_line = macro_line.replace(arg_name, arg_values[i])
            output_program.append(macro_line)
    else:
        output_program.append(line)

output = '\n'.join(output_program)
print(output)
