estudantes = {'Nome': str(input('Nome: '))}
estudantes['Média'] = float(input(f'Média de {estudantes["Nome"]}: '))
Situação = ''
if estudantes['Média'] >= 7:
    estudantes['Situação'] = 'APROVADO(A)'
else:
    estudantes['Situação'] = 'REPROVADO(A)'
print('-=' * 30)
for k, v in estudantes.items():
    print(f'  - {k} é igual a {v}')

# print(f'Nome é igual a {estudantes["nome"]}')
# print(f'Média é igual a {estudantes["media"]}')
# print(f'Situação é igual a {estudantes["situacao"]}')
