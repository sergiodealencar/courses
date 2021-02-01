lista = []
for c in range(0, 5):
    n = (int(input('Digite um valor: ')))
    if c == 0 or n > lista[-1]:  # -1 é o último valor da lista
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')

#     if c >= 1:
#         lista.append(novo)
#         lista.sort()
#         if novo == max(lista):
#             print('Adicionado ao final da lista...')
#         else:
#             print(f'Adicionado na posição {lista.index(novo)} da lista...')
# print('-='*30)
# print(f'Os valores digitados em ordem foram {lista}')
