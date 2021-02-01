lista = [[], [], []]
for c in range(0, 3):
    for p in range(0, 3):
        lista[c].append(int(input(f'Digite um valor para [{c}, {p}]: ')))
print('-='*20)
for c in range(0, 3):
    for p in range(0, 3):
        print(f'[ {lista[c][p]:^5} ]', end='')  # para centralizar: ^5
    print()
