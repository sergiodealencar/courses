frase = input('Digite uma frase: ')
counta = frase.count('a')
print('A letra "a" aparece {} vezes nesta frase.' .format(counta))
index_start = frase.find('a')
print('A primeira ocorrência de a é na posição {}' .format(index_start + 1))
print('A última ocorrência de a é na posição {}' .format(frase.rfind('a') + 1))
