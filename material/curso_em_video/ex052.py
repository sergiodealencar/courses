count_div = 0
num = int(input("Digite um número inteiro: "))
for i in range(1, num + 1):
    if (num % i) == 0:
        print('\033[33m', end=' ')
        count_div += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end='')
print('\n\033[mO número {} foi divisível {} vez(es).'.format(num, count_div))
if count_div == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
