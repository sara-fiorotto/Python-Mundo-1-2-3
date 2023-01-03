from random import randint
from time import sleep
jogo1 = list()
jogo2 = list()
jogos = int(input('Quantos jogos você quer?'))
for c in range(1, jogos+1):
    while True:
        sort = randint(1, 60)
        if sort not in jogo1:
            jogo1.append(sort)
        if len(jogo1) == 6:
            break
    jogo2.append(jogo1[:])
    jogo1.sort()
    print(f'O jogo {c} é: {jogo1}')
    jogo1.clear()
    sleep(1)
print(jogo2)
