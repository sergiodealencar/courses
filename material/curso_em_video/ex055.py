maior = 0
menor = 0
for c in range(1, 6):
	w = float(input('Peso {} (em Kg)? '.format(c)))
	if c == 1:
		maior = w
		menor = w
	else:
		if w > maior:
			maior = w
		if w < menor:
			menor = w
print('\nMaior peso: {}Kg'.format(maior))
print('Menor peso: {}Kg'.format(menor))
