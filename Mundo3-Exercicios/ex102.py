def fatorial(n, show=False):
    """
    -> Essa função é para calular o fatorial de um número!
    :param n: O valor a ser calculado dentro da função
    :param show: Opcional, mostra ou não a conta feita
    :return : O valor total do fatorial de n
    """
    fator = 1
    i = 2
    while i <= n:
        fator = fator * i
        i = i + 1
    if show:
        for p in range(n, 0, -1):
            print(f'{p}', end=' ')
            if p > 1:
                print('x', end=' ')
        print('=', fator)
    else:
        print(f'O resultado é {fator}')


help(fatorial)
####fatorial(8, show=True)
