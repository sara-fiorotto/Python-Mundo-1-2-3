valores = list()
maior = menor = 0
for p, v in enumerate(range(0, 5)):
    valores.append(int(input(f'Na posição {p} digite um valor:')))
print(valores)
print(f'o maior valor é {max(valores)} na posição', end=' ')
for p1, v1 in enumerate(valores):
    if v1 == max(valores):
        print(f' {p1}..', end='')
print(f'\nO menor valor é {min(valores)} na posição', end=' ')
for p1, v1 in enumerate(valores):
    if v1 == min(valores):
        print(f'{p1}...', end=' ')