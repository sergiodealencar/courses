from random import randint
tupla = (randint(0, 100), randint(0, 100), randint(0, 100),
         randint(0, 100), randint(0, 100))
print(f'Os valores sorteados foram: ', end='')
for n in tupla:
    print(f'{n} ', end='')
# maior = 0
# menor = 0
# for c in range(0, 4):
#     if c == 0:
#         menor = tupla[c]
#         maior = tupla[c]
#     c += 1
#     if tupla[c] > maior:
#         maior = tupla[c]
#     if tupla[c] < menor:
#         menor = tupla[c]
# print('\nO maior valor sorteado foi', maior)
# print('O menor valor sorteado foi', menor)
print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')
