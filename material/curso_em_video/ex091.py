from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
print('Valores sorteados:')
jogo['jogador1'] = randint(1, 6)
jogo['jogador2'] = randint(1, 6)
jogo['jogador3'] = randint(1, 6)
jogo['jogador4'] = randint(1, 6)
for c, v in jogo.items():
    print(f'   O {c} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i + 1}o lugar: {v[0]} com {v[1]}.')
    sleep(1)
