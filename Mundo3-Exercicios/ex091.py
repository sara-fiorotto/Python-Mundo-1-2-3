from random import randint
from time import sleep
from operator import itemgetter
jogo = {'01': int(randint(1, 6)), '02': int(randint(1, 6)), '03': int(randint(1, 6)), '04': int(randint(1, 6))}
for j, s in jogo.items():
    print(f'O jogador {j} tirou: {s}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('---- RANNNNKINNNNG!!!----')
for i, v in enumerate(ranking):
    print(f'    {i+1}ª Lugar: Jogador {v[0]} com {v[1]} ')
    sleep(1)