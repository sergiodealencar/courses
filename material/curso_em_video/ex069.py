cont_18 = cont_M = cont_F = 0
while True:
    print('-' * 25)
    print('   CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-' * 25)
    if idade >= 18:
        cont_18 += 1
    if sexo == 'M':
        cont_M += 1
    if sexo == 'F' and idade < 20:
        cont_F += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {cont_18}')
print(f'Ao todo temos {cont_M} homens cadastrado(s).')
print(f'E temos {cont_F} mulher(es) com menos de 20 anos.')
