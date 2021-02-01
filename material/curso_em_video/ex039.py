from datetime import date

atual = date.today().year
nasc = int(input('Qual é o ano do seu nascimento? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} ano(s) em {}.'.format(nasc, idade, atual))
if idade < 18:
    print('Você ainda não tem 18 anos. Faltam {:.0f} ano(s) para você se alistar.'.format(18 - idade))
elif idade == 18:
    print('É hora de você se alistar.')
elif idade > 18:
    print('Já passou da hora de você se alistar. Você deveria ter se alistado {:.0f} anos atrás.'.format(idade - 18))
