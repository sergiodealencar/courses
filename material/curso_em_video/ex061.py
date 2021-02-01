print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
i = int(input('Qual é o primeiro termo? '))
r = int(input('Qual é a razão da progressão aritmética? '))
cont = 1
while cont <= 10:
    print('{} -> '.format(i), end='')
    i += r
    cont += 1
print('ACABOU')

