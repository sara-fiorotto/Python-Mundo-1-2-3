def area(lag, c):
    a2 = lag * c
    print('***' * 10)
    print(f'A area do Terreno {lag}x{c} é de {a2}m²')


area(lag=float(input('LARGURA (m):')), c=float(input('COMPRIMENTO (m):')))
