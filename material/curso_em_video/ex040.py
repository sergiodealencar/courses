nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

print('Tirando {:.1f} e {:.1f}, a média do estudante é {:.1f}.'.format(nota1, nota2, media))

if media < 5:
    print('O estudante está \033[0:31mREPROVADO')
elif 5 <= media <= 6.9:
    print('O estudante está de \033[0:31mRECUPERAÇÃO')
else:
    print('O estudante está \033[0:32mAPROVADO')
