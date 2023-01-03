n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
n3 = int(input('Digite um número:'))
n4 = int(input('Digite um número:'))
t1 = (n1, n2, n3, n4)
print(f'o nove apareceu {t1.count(9)} vezes')
if 3 in t1:
    print(f'O primeiro 3 esta na posição {t1.index(3) + 1}')
else:
    print('O 3 não esta inserido na tupla')
print('Os números pares são:', end=' ')
for par in t1:
    if par % 2 == 0:
        print(par, end=' ')