def metade(x):
    x = x / 2
    return x


def dobro(x):
    x = x * 2
    return x


def aumentando(x, por):
    tot = x + ((x / 100) * por)
    return tot


def diminuindo(x, por):
    tot = x - ((x / 100) * por)
    return tot


def moeda(x):
    x = f'R${x}'
    return x


