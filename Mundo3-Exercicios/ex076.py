tupla = ('Pão', 5, 'Leite', 10, 'Café', 8, 'Manteiga', 6)
print('-' * 40)
print(f'\033[1;36;40m{"LISTAGEM DE PREÇO":^40}\033[m')
print('-' * 40)
for l1 in range(0, len(tupla)):
    if l1 % 2 == 0:
        print(f'{tupla[l1]:.<30}', end='')
    else:
        print(f'\033[1;32mR${tupla[l1]:>6.2f}\033[m')

