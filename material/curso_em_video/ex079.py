valores = list()
resp = 'S'
novo = 0
while resp in 'S':
    novo = (int(input('Digite um valor: ')))
    if novo in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        valores.append(novo)
    resp = str(input('Quer continuar? [S/N] ')).upper()
valores.sort()
print(f'Você digitou os valores {valores}')
