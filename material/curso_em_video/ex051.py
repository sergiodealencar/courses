print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
i = int(input('Qual é o primeiro termo? '))
r = int(input('Qual é a razão da progressão aritmética? '))
for c in range(i, (i + (r * 10)), r):
    print(c, end=' -> ')
print('ACABOU')
