times = ('Cruzeiro', 'Corinthians', 'Fluminense', 'Internacional',
         'Sport', 'Santos', 'Goiás', 'São Paulo', 'Atlético-PR',
         'Grêmio', 'Atlético-MG', 'Palmeiras', 'Botafogo', 'Criciúma',
         'Chapecoense', 'Vitória', 'Coritiba', 'Flamengo', 'Bahia',
         'Figueirense')
print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
# for t in (times):
#     print(t)
print('-='*15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
chap = times.index('Chapecoense') + 1
print(f'O Chapecoense está na {chap}ª posição.')
