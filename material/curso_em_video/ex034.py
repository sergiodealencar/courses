s = float(input('Qual é o seu salário? R$'))
if s > 1250:
    novo = s + (s * 10 / 100)
else:
    novo = s + (s * 15 / 100)
print('Quem ganhava R${:.2f} ganha agora R${:.2f}.' .format(s, novo))
