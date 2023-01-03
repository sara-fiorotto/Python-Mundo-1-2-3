from random import choices, choice
maior = menor = 0
lista = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('Os valores sorteados são :')
for s in range(0, 5):
    t = choice(lista)
    print(t, end=' ')
    if s == 1:
        maior = menor = t
    else:
        if t > maior:
            maior = t
        if t < menor:
            menor = t
print(f'\nO maior valor é {maior}')
print(f'O menor valor é {menor}')
