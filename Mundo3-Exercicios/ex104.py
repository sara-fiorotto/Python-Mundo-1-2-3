'''def leiaint(p):   #meu código"
    "while True:
        if p.isnumeric():
            print(f'Você digitou {p}')
            break
        else:
            print('ERRO, TENTE NOVAMENTE')
            p = str(input('Digite um numero:'))
n = input('Digite um numero: ')
leiaint(n)'''


def leiaint(n):
    while True:
        x = input(n)
        if x.isnumeric():
            print(f'Você digitou {x}')
            break
        else:
            print('ERRO, TENTE NOVAMENTE')


p = leiaint('Digite um numero: ')
