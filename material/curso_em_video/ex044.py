print('\n', '=' * 10, 'LOJA DA LILI', '=' * 10)

preco = float(input('\nQual é o preço do produto? R$'))

opt = int(input('''\nSelecione uma das seguintes opções de pagamento:\n
\t[ 1 ] à vista dinheiro/cheque: 10% de desconto
\t[ 2 ] à vista no cartão: 5% de desconto
\t[ 3 ] em até 2x no cartão: preço normal
\t[ 4 ] 3x ou mais no cartão: 20% de juros
\n\tQual é a opção: '''))

if opt == 1:
    valor = preco - (preco * 10 / 100)
elif opt == 2:
    valor = preco - (preco * 5 / 100)
elif opt == 3:
    valor = preco
    valor_parcelado = preco / 2
    print('Sua compra será parcelada em 2x de R${} SEM JUROS.'.format(valor_parcelado))
elif opt == 4:
    parcela = int(input('\nQuantas parcelas? '))
    valor = preco + ((preco * 20) / 100)
    valor_parcelado = valor / parcela
    print('Sua compra será parcelada em {:.0f}x de R${:.2f} COM JUROS.'.format(parcela, valor_parcelado))
else:
    valor = 0
    print('\nOPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, valor))
