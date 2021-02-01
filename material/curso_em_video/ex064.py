n = soma = cont = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
        cont += 1
    else:
        print('\nVocê digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
print('\nFIM')


# n = int(input('Digite um número [999 para parar]: '))
# while n != 999:
#     soma += n
#     cont += 1
#     n = int(input('Digite um número [999 para parar]: '))
# print('\nVocê digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
