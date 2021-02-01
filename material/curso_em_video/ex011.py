alt = float(input('Qual é a altura da parede (em m)? '))
lar = float(input('E a largura (em m)? '))
area = alt * lar
print('A parede tem uma área de {} metros quadrados.' .format(area))
tinta = float(area/2)
print('Você vai precisar de {} litro(s) de tinta para pintar essa parede.' .format(tinta))
