def metade(x, f=False):
    x = x / 2
    if f:
        x = moeda(x)
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


def resumo(n, a, d):
    print(f'\033[1;35m  {"RESUMO DO VALOR":^25}\033[m')
    print('-' * 30)
    print(f'\033[1;38mPreço analisado:  {moeda(n):^15}')
    print(f'Dobro do preço:   {dobro(n, True):^15}')
    print(f'Metade do preço:  {metade(n, True):^15}')
    print(f'{a}% de aumento:   {aumentando(n, a, True):^15}')
    print(f'{d}% de redução:   {diminuindo(n, d, True):^15}\033[m')
    print('-' * 30)


