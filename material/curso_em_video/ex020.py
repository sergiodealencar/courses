from random import shuffle
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação é a seguinte:\n1: {}\n2: {}\n3: {}\n4: {}' .format(lista[0], lista[1], lista[2], lista[3]))

