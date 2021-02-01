print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
i = int(input('Qual é o primeiro termo? '))
r = int(input('Qual é a razão da progressão aritmética? '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(i), end='')
        i += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos.'.format(total))
