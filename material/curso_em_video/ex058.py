from random import randint
from time import sleep
n = randint(0, 10)
print('-=-' * 20)
print('   Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
nuser = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(0.5)
s = 1
while nuser != n:
    if nuser < n:
        nuser = int(input('Mais... Tente de novo: '))
    elif nuser > n:
        nuser = int(input('Menos... Tente de novo: '))
    print('PROCESSANDO...')
    sleep(0.5)
    s += 1
print('Você ganhou! Foram necessárias {} tentativas para você ganhar!'.format(s))
print('--FIM--')


# outra possibilidade:
# acertou = False
# while not acertou:
# dentro, depois de acertar, põe: acertou == True