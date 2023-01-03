def metade(x, f=False):
    x = x / 2
    if f:
        x = f'R${x}'
    return x


def dobro(x, f=False):
    x = x * 2
    if f:
        x = f'R${x}'
    return x


def aumentando(x, por, f=False):
    tot = x + ((x / 100) * por)
    if f:
        tot = f'R${tot}'
    return tot


def diminuindo(x, por, f=False):
    tot = x - ((x / 100) * por)
    if f:
        tot = f'R${tot}'
    return tot


def moeda(x):
    x = f'R${x}'
    return x

