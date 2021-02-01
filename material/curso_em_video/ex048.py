print('\nNúmeros ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500: \n')
s = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        s += c  # s = s + c
        count += 1
print('\nA soma de todos os {} valores solicitados é {}.'.format(count, s))
print('\nFIM')
