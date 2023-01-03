numeros = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor:'))
    if n % 2 == 0:
        numeros[0].insert(0, n)
    else:
        numeros[1].insert(0, n)
numeros[0].sort()
numeros[1].sort()
print(numeros[0])
print(numeros[1])
