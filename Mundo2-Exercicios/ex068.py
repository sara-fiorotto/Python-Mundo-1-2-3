from random import randint
p = c = 0
resp = ''
while True:
    pc = randint(0, 10)
    j = int(input('Digite um número :'))
    r = str(input('Par ou Ìmpar [P/I]:')).upper()[0]
    p = pc + j
    if p % 2 == 0:
        resp = 'PAR'
    else:
        resp = 'IMPAR'
    print(f'Você jogou {j} o computador escolheu {pc}', end=' ')
    print(f'.O total {p} DEU {resp}')
    if resp == 'PAR' and r == 'P' or resp == 'IMPAR' and r == 'I':
        print('VOCÊ GANHOU ... VAMOS DE NOVO!!')
        print('-' * 20)
        c += 1
    else:
        break
print(f'GAME OVER, você venceu {c} vezes')
