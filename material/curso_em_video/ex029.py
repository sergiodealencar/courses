v = float(input('Qual é a velocidade do carro (em km/h)? '))
if v > 80:
    print('Você foi multado por exceder o limite '
          'permitido de 80km/h! Terá que pagar uma multa de R${:.2f}' .format((v-80)*7))
else:
    print('Tenha um bom dia! Dirija com segurança!')
print('--FIM--')
