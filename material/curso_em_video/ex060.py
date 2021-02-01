n = int(input('Digite um número para calcular seu fatorial: '))
mult = n
print('\n{}! = '.format(n), end='')
while n != 1:
    print('{} x '.format(n), end='')
    n -= 1
    mult *= n
print('1 = ', end='')
print(mult)

# from math import factorial
# n = int(input('Digite um número para calcular seu Fatorial: '))
# f = factorial(n)
# print('O fatorial de {} é {}.'.format(n, f))
