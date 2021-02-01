nome = input('Digite seu nome completo: ')
print('Nome em letras maiúsculas: {}' .format(nome.upper().strip()))
print('Nome em letras minúsculas: {}' .format(nome.lower().strip()))
print('Total de letras: {}' .format(len((nome.replace(" ", "")))))
nome_s = nome.split()
print('O primeiro nome tem {} letras.' .format(len(nome_s[0])))


