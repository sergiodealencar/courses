valores = []
while True:
    novo = (int(input('Digite um valor: ')))
    valores.append(novo)
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp in 'Nn':
        break
valores.sort(reverse=True)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
