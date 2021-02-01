print('-'*26)
print('  Sequência de Fibonacci')
print('-'*26)
vezes = int(input('Quantos termos você quer mostrar? '))
f1 = 1
f2 = 1
i = 0
print('~'*36)
if vezes == 1:
    print('0 -> ', end='')
elif vezes == 2:
    print('0 -> 1 -> ', end='')
else:
    print('0 -> 1 -> 1 -> ', end='')
    while i < vezes - 3:
        nacci = f1 + f2
        print(nacci, '-> ', end='')
        f2 = f1
        f1 = nacci
        i += 1
print('FIM')
print('~'*36)
