expressao = str(input('Digite uma expressão: ')).strip().replace(" ", "")
termos = []
forward = 0
reverse = 0
for c in range(0, len(expressao)):
    termos.append(expressao[c])
    if "(" in termos[c]:
        forward += 1
    elif ")" in termos[c]:
        reverse += 1
if forward == reverse:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
