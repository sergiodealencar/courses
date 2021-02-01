from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 13)
print('  Computador jogou {}'.format(itens[computador]))
print('  ALICE jogou {}'.format(itens[jogador]))
print('-=' * 13)
if computador == 0:  # computador jogou pedra
    if jogador == 0:
        print('\033[1:34mEMPATE')
    elif jogador == 1:
        print('\033[1:33mALICE VENCE')
    elif jogador == 2:
        print('\033[1:31mCOMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:  # computador jogou papel
    if jogador == 0:
        print('\033[1:31mCOMPUTADOR VENCE')
    elif jogador == 1:
        print('\033[1:34mEMPATE')
    elif jogador == 2:
        print('\033[1:33mALICE VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:  # computador jogou tesoura
    if jogador == 0:
        print('\033[1:33mALICE VENCE')
    elif jogador == 1:
        print('\033[1:31mCOMPUTADOR VENCE')
    elif jogador == 2:
        print('\033[1:34mEMPATE')
    else:
        print('JOGADA INVÁLIDA')
