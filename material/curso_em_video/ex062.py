print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
i = int(input('Qual é o primeiro termo? '))
r = int(input('Qual é a razão da progressão aritmética? '))
s = 1
n = 10
more = 1
while s <= n:
    print(i, end=' -> ')
    i += r
    s += 1
while more != 0:
    print('PAUSA')
    more = int(input('\nQuantos termos mais você gostaria de ver? '))
    n = n + more
    while s <= n:
        print(i, end=' -> ')
        i += r
        s += 1
print('Progressão finalizada com {} termos mostrados.'.format(n))

