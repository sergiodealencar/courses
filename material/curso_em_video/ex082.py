valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp in 'N':
        break
print(f'A lista completa é {valores}')
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-='*30)
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
