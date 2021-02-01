print('--'*15)
print('      LOJA SUPER BARATÃO')
print('--'*15)
total = caro = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    total += preço
    cont += 1
    if preço >= 1000:
        caro += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('------- FIM DO PROGRAMA -------')
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {caro} produto(s) custando mais de R$1000.00.')
print(f'O produto mais barato foi {barato}, que custa R${menor:.2f}.')
