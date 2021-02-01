soma = 0
i = 0
cont = ''
maior = 0
menor = 0
while cont != 'N':
    n = int(input('Digite um número: '))
    soma += n
    i += 1
    if i == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SN':
        print('Resposta incorreta! Digite novamente!')
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()
print('Você digitou {} números e a média foi {}.'.format(i, (soma / i)))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
