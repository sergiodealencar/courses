s = str(input('Qual é o seu sexo? [M/F] ')).strip().upper()[0]  # [0] só pega a primeira letra
while s not in 'FM':
    s = str(input('Sexo inválido! Digite novamente: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(s))
