spre = str(input('Digite um texto: '))
s = (spre.replace(" ", "")).strip().upper()
# palind = ""
# len = len(s)
# for c in range(-1, -len - 1, -1):
# 	palind += s[c]

palind = s[::-1]	#inverso da palavra/frase

print('O inverso de {} é {}.'.format(s, palind))
if s == palind:
	print("A frase digitada é um palíndromo!")
else:
	print('A frase digitada não é um palíndromo!')