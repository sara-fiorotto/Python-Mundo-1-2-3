matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for num in matriz[0]:
    if num % 2 == 0:
        soma += num
for num in matriz[1]:
    if num % 2 == 0:
        soma += num
for num in matriz[2]:
    if num % 2 == 0:
        soma += num
print(f'soma total é de {soma}')
for pos, num in enumerate(matriz[0]):
    if pos == 2:
        soma2 += num
for pos, num in enumerate(matriz[1]):
    if pos == 2:
        soma2 += num
for pos, num in enumerate(matriz[2]):
    if pos == 2:
        soma2 += num
print(f'A soma da terceira coluna é {soma2}')
print(f'o maior valor da segunda linha é {max(matriz[1])}')
