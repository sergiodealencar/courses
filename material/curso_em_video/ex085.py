lista = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores ímpres digitados foram: {sorted(lista[1])}')

# meu código (funcionou também):
# lista = [[], []]
# temp = []
# for c in range(1, 8):
#     temp.append(int(input(f'Digite o {c}o valor: ')))
#     if temp[c] % 2 == 0:
#         lista[0].append(temp[c])
#     else:
#         lista[1].append(temp[c])
# print('-=' * 30)
# sorted(lista)
# print(f'Os valores pares digitados foram: {sorted(lista[0])}')
# print(f'Os valores ímpres digitados foram: {sorted(lista[1])}')
