from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')

# Minha versão:
# from random import randint
# print('=-' * 13)
# print('VAMOS JOGAR PAR OU ÍMPAR?')
# print('=-' * 13)
# i = 0
# while True:
#     valor = int(input('Diga um número: '))
#     escolha = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
#     while escolha not in 'PI':
#         print('Valor incorreto!')
#         escolha = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
#     if escolha == 'P':
#         escolha = 'PAR'
#     if escolha == 'I':
#         escolha = 'ÍMPAR'
#     computador = randint(0, 10)
#     soma = valor + computador
#     print('--' * 13)
#     if soma % 2 == 0:
#         resultado = 'PAR'
#     else:
#         resultado = 'ÍMPAR'
#     if resultado == escolha:
#         print(f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU {resultado}.')
#         print('--' * 13)
#         print('Você VENCEU!')
#         print('Vamos jogar novamente...')
#         print('=-' * 13)
#         i += 1
#     else:
#         break
# print(f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU {resultado}.')
# print('--' * 13)
# print('Você PERDEU!')
# print('=-' * 13)
# print(f'GAME OVER! Você venceu {i} vez(es).')