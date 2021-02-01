print('--' * 22)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('--' * 22)
listagem = (
    ' Lápis', 1.75,
    ' Borracha', 2.00,
    ' Caderno', 15.90,
    ' Estojo', 25.00,
    ' Transferidor', 4.20,
    ' Compasso', 9.99,
    ' Mochila', 120.32,
    ' Canetas', 22.30,
    ' Livro', 34.90)
n = 0
while n <= 17:
    print(f'{listagem[n]:.<33} R$ {listagem[n + 1]:>6.2f}')
    n += 2
print('--' * 22)
