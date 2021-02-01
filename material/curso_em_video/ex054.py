from datetime import date
ano = date.today().year
s = 0
i = 0
for c in range(1, 8):
	a = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
	if ano - a >= 21:
		s += 1
	else:
		i += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(s))
print('E também tivemos {} pessoas menores de idade.'.format(i))
