from random import randint
from time import sleep

jogo = {'Jairo': randint(1, 6), 'Carla': randint(1, 6), 'Amanda': randint(1, 6), 'Augusto': randint(1, 6)}
print('Valores sorteados:')
ranking = list()
for k, v in jogo.items():
    print(f'{k} tirou {v} nos dados')
    sleep(1)
ranking = sorted(jogo.items(), key=lambda item: item[1], reverse=True)
print('-=' * 20)
print(ranking)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f' {i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)