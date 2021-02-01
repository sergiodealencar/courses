print('-*' * 20)
print('        Analisador de Triângulos')
print('-*' * 20 ,'\n')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
cond1 = b - c < a < b + c
cond2 = a - c < b < a + c
cond3 = a - b < c < a + b
if cond1 is True and cond2 is True and cond3 is True:
    print('\nEssa combinação de lados forma um triângulo!')
else:
    print('\nEssa combinação de lados não forma um triângulo!')
