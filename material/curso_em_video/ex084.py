temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp in 'N':
        break
print('-=' * 30)
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai} Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men} Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()

# lista = list()
# dados = []
# while True:
#     lista.append(str(input('Nome: ')))
#     lista.append(float(input('Peso: ')))
#     dados.append(lista[:])
#     lista.clear()
#     cont = str(input('Quer continuar? [S/N] ')).upper()
#     if cont in 'N':
#         break
# print('-='*30)
# print(f'Ao todo você cadastrou {len(dados)} pessoas.')
# mai = men = dados[0][1]
# for p in dados:
#     if p[1] > mai:
#         mai = p[1]
#     if p[1] < men:
#         men = p[1]
# print(f'O maior peso foi de {mai}. Peso de ', end='')
# for p in dados:
#     if p[1] == mai:
#         print(p[0])
# print(f'O menor peso foi de {mai}. Peso de ', end='')
# for p in dados:
#     if p[1] == men:
#         print(p[0])
