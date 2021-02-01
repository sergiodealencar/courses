valor = float(input('Qual é o valor da casa que você quer comprar? R$'))
salario = float(input('Qual é o valor do seu salário? R$'))
anos = int(input('Em quantos anos você quer pagá-la? '))

prestacao = valor / (anos * 12)

salario30 = salario * 30 / 100

if prestacao <= salario30:
    print('O valor da prestação é de R${:.2f}'.format(prestacao))
    print('\n\033[0:32mEmpréstimo pode ser CONCEDIDO!')
else:
    print('O valor da prestação (R${:.2f}) é superior a 30% do seu salário (R${}). '
          '\n\033[0:31mInfelizmente, não será possível fazer o empréstimo.'.format(prestacao, salario30))
