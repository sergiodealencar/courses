dist = float(input('Qual é a distância da sua viagem em Km? '))
if dist <= 200:
    print('Sua pasagem irá custar R${:.2f}.' .format(dist*0.50))
else:
    print('Sua passagem irá custar R${:.2f}' .format(dist*0.45))
print('--- FIM ---')
