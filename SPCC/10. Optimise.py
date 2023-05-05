expression = "2 + 2 * 4"
tokens = expression.split()
for i in range(len(tokens)):
    if tokens[i].isdigit():
        tokens[i] = int(tokens[i])
while len(tokens) > 1:
    for i in range(len(tokens)):
        if tokens[i] == "*":
            tokens[i-1] = tokens[i-1] * tokens[i+1]
            del tokens[i:i+2]
            break
        elif tokens[i] == "/":
            tokens[i-1] = tokens[i-1] / tokens[i+1]
            del tokens[i:i+2]
            break
    else:
        break
while len(tokens) > 1:
    for i in range(len(tokens)):
        if tokens[i] == "+":
            tokens[i-1] = tokens[i-1] + tokens[i+1]
            del tokens[i:i+2]
            break
        elif tokens[i] == "-":
            tokens[i-1] = tokens[i-1] - tokens[i+1]
            del tokens[i:i+2]
            break
    else:
        break
result = tokens[0]
print(result)
