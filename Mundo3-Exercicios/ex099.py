def maio(*num):

    maior = 0
    pos = 0
    post = 0
    print('Valores passados foram:', end='')
    while post < len(num[0]):
        print(f'{num[0][post]} ', end=' ')
        post += 1
    print()
    print(f'{len(num[0])} valores foram informados e o maior é....', end='')
    while pos < len(num[0]):
        if pos == 0:
            maior = num[0][pos]
        else:
            if num[0][pos] > maior:
                maior = num[0][pos]

        pos += 1
    print(maior)


valores = [2, 3, 5, 6]
maio(valores)
valores = [0]
maio(valores)
valores = [91, 52, 26, 44, 100]
maio(valores)
