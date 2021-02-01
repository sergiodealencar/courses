s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o valor {}: '.format(c)))
    if (n % 2) == 0 and n != 0:
        s += n  # s = s + n
        cont += 1
print('\nVocê informou {} número(s) PAR(ES), e o somatório deles foi {}'.format(cont, s))
