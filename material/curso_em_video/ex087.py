lista = [[], [], []]
par = terc_col = mai = 0
for c in range(0, 3):
    for p in range(0, 3):
        lista[c].append(int(input(f'Digite um valor para [{c}, {p}]: ')))
        if lista[c][p] % 2 == 0:
            par += lista[c][p]
print('-='*20)
for c in range(0, 3):
    for p in range(0, 3):
        print(f'[  {lista[c][p]:^5}  ]', end='')
    print()
print('-='*20)
print(f'A soma dos valores pares é {par}.')
for p in range(0, 3):
    terc_col += lista[p][2]
print(f'A soma dos valores da terceira coluna é {terc_col}.')
for c in range(0, 3):
    if c == 0:
        mai = lista[1][c]
    elif lista[1][c] > mai:
        mai = lista[1][c]
print(f'O maior valor da segunda linha é {mai}.')
