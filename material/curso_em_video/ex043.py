peso = float(input('Qual é seu peso (em Kg)? '))
altura = float(input('Qual é sua altura (em m)? '))
imc = peso / (altura ** 2)

print('O seu IMC é {:.1f}. O seu status é o seguinte:'.format(imc))

if imc < 18.5:
    print('\033[0:31mAbaixo do Peso')
elif 18.5 <= imc < 25:
    print('\033[0:32mPeso Ideal')
elif 25 <= imc < 30:
    print('\033[0:31mSobrepeso')
elif 30 <= imc < 40:
    print('\033[0:31mObesidade')
else:
    print('\033[1:31mObesidade mórbida')
