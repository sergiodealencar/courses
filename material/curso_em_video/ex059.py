from time import sleep

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print('''\n>>>Selecione uma das opções abaixo: 
    [1] somar
    [2] multiplicar
    [3] maor
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('Opção: '))
    print('PROCESSANDO...')
    sleep(1.0)
    if opcao == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1 + n2))
        print('=-=' * 12)
    elif opcao == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
        print('=-=' * 12)
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
            print('=-=' * 12)
        else:
            print('{} é maior que {}.'.format(n2, n1))
            print('=-=' * 12)
    elif opcao == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
print('Fim do programa! Volte sempre!')
print('=-=' * 12)
