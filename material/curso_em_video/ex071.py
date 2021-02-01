# print('=='*15)
# print('{:^30}'.format('BANCO PATINHAS'))
# print('=='*15)
# nota50 = nota20 = nota10 = nota1 = 0
# valor = int(input('Que valor você quer sacar? R$'))
# while valor != 0:
#     while valor >= 50:
#         valor -= 50
#         nota50 += 1
#     while valor >= 20:
#         valor -= 20
#         nota20 += 1
#     while valor >= 10:
#         valor -= 10
#         nota10 += 1
#     while valor >= 1:
#         valor -= 1
#         nota1 += 1
# if nota50:
#     print(f'Total de {nota50} cédula(s) de R$50.')
# if nota20:
#     print(f'Total de {nota20} cédula(s) de R$20.')
# if nota10:
#     print(f'Total de {nota10} cédula(s) de R$10.')
# if nota1:
#     print(f'Total de {nota1} cédula(s) de R$1.')
# print('=='*15)
# print('Volte sempre ao BANCO PATINHAS! Tenha um bom dia!')


print('=='*15)
print('{:^30}'.format('BANCO PATINHAS'))
print('=='*15)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO PATINHAS! Tenha um bom dia!')
