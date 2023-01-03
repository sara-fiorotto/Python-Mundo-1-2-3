while True:
    n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
         'sete', 'oito', 'nove', 'dez')
    n0 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    resp = int(input('Digite um número:'))
    while resp not in n0:
        resp = int(input('Tente novamente. Digite um número'))
    print('Você escolheu o número {}'.format(n[resp]))
    resp1 = str(input('Deseja continuar? [S/N]')).upper()[0]
    if resp1 in 'N':
        break
print('Fim')