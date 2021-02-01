soma_idade = 0
sexo = ''
age_oldest = 0
name_oldest = 0
cont_mulheres = 0
for c in range(1, 5):
    print('\n----- {}ª PESSOA ----- '.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()
    soma_idade += idade
    if c == 1 and sexo in 'Mm':
        age_oldest = idade
        name_oldest = nome
    if idade > age_oldest and sexo in 'Mm':
        age_oldest = idade
        name_oldest = nome
    if sexo in 'Ff' and idade < 20:
        cont_mulheres += 1
print('A média de idade do grupo é de {} anos.'.format(soma_idade/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(age_oldest, name_oldest))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(cont_mulheres))
