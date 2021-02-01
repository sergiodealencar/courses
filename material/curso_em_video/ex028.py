from random import randint
from time import sleep

n = randint(0, 5)
print('-=-' * 20)
print('   Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
nuser = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if nuser == n:
    print('Você adivinhou! PARABÉNS!!!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(n, nuser))
print('--FIM--')
