n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n1 > n2 and n1 > n3:
    print('o maior é ', n1)
if n2 > n1 and n2 > n3:
    print('o maior é ', n2)
if n3 > n1 and n3 > n2:
    print('o maior é ', n3)
else:
    if n1 == n2 and n1 > n3:
        print('o maior é ', n1)
    if n1 == n3 and n1 > n2:
        print('o maior é ', n1)
    if n2 == n3 and n2 > n1:
        print('o maior é ', n2)
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if menor != n1 or menor != n2 or menor != n3:
    print('o menor é ', menor)
else:
    print(' todos iguais!')
