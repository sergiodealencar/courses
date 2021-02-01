dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
total_pagar = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}' .format(total_pagar))
#print('O total a pagar é de R${:.2f}' .format((dias * 60) + (km * 0.15)))


