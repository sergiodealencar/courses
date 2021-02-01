dec = int(input('Digite um número inteiro: '))

opt = (int(input('''Escolha uma das bases para convsersão:\n
\t[ 1 ] converter para BINÁRIO
\t[ 2 ] converter para OCTAL
\t[ 3 ] converter para HEXADECIMAL
\n\tSua opção: ''')))


if opt == 1:
    print('\n{} convertido para BINÁRIO é igual a {}.'.format(dec, bin(dec)[2:]))
elif opt == 2:
    print('\n{} convertido para OCTAL é igual a {}.'.format(dec, oct(dec)[2:]))
elif opt == 3:
    print('\n{} convertido para HEXADECIMAL é igual a {}.'.format(dec, hex(dec)[2:]))
else:
    print('\n\033[0:31mOpção inválida. Tente novamente.')
