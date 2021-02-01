primeiro = int(input('Diga o primeiro valor inteiro: '))
segundo = int(input('Diga o segundo valor inteiro: '))

if primeiro > segundo:
    print('\nO PRIMEIRO valor é maior.')
elif segundo > primeiro:
    print('\nO SEGUNDO valor é maior.')
else:
    print('\nNão existe valor maior, os dois são IGUAIS.')
