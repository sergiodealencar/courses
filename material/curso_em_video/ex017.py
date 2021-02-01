import math
cat_op = float(input('Qual é o valor do cateto oposto? '))
cat_adj = float(input('Qual é o valor do cateto adjacente? '))
print('O comprimento da hipotenusa deste triângulo é {:.2f}.' .format(math.hypot(cat_op, cat_adj)))