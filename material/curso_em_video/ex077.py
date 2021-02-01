palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

# cont = len(palavras)
# for i in range(0, cont):    # for pegando todas as palavras (0 a 2)
#     print('Na palavra', palavras[i].upper(), 'temos', end=' ')
#     for c in range(0, len(palavras[i])):  # for pegando
#         # print(palavras[i][c])
#         if palavras[i][c] in 'aeiou':
#             print(palavras[i][c], end=' ')
#     print('')
