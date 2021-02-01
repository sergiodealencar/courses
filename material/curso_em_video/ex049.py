n = int(input('\nDigite um número inteiro: '))
print('-' * 13)
for c in range(1, 11):
    print('{} x {:2} = {}' .format(n, c, (n*c)))
print('-' * 13)
