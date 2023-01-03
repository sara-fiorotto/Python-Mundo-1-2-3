pessoas = list()
total = list()
maior = menor = 0
while True:
    pessoas.append(str(input('Nome:')))
    pessoas.append(int(input('Peso KG: ')))
    total.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Deseja continuar?[S/N]'))
    if resp in 'Nn':
        break
print(f'Ao todo você cadastrou {len(total)} pessoas')
for pos, p in enumerate(total):
    if pos == 0:
        maior = menor = p[1]
    else:
        if p[1] >= maior:
            maior = p[1]
        if p[1] <= menor:
            menor = p[1]
print(f'O maior peso foi de {maior}KG. Peso de ', end=' ')
for p in total:
    if maior in p:
        print('"', p[0], '"', end=' ')
print(f'\nO menor peso foi de {menor}KG. Peso de ', end=' ')
for p in total:
    if menor in p:
        print('"', p[0], '"', end=' ')

