def maiores(*num):
    cont = maior = 0
    print('Os valores informados foram..')
    for v in num:
        print(f'{v}...', end='')
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor citado foi {maior}')


maiores(1, 2, 3)
maiores(8, 25, 98, 0)
