# numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#            11, 12, 13, 14, 15, 16, 17, 17,
#            19, 20)
# extenso = ('zero', 'um', 'dois', 'três', 'quatro',
#            'cinco', 'seis', 'sete', 'oito', 'nove',
#            'dez', 'onze', 'doze', 'treze', 'quatorze',
#            'quinze', 'dezesseis', 'dezesete', 'dezoito',
#            'dezenove', 'vinte')
# usuario = int(input('Digite um número entre 0 e 20: '))
# while usuario not in numeros:
#     usuario = int(input('Tente novamente. Digite um número entre 0 e 20: '))
# print(f'Você digitou o número {extenso[usuario]}.')


cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezesete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}.')
