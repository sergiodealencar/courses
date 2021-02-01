tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
print(f'Você digitou os valores {tupla}')
n9 = tupla.count(9)
if n9 >= 1:
    print(f'O valor 9 apareceu {n9} vez(es).')
else:
    print('O valor 9 apareceu 0 vezes.')
if 3 in tupla:
    posicao3 = tupla.index(3) + 1
    print(f'O valor 3 apareceu na {posicao3}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
