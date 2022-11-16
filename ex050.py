s = 0
for c in range(0, 6):
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        s += n
print(f'O resultado da soma dos números pares é {s},'
      ' desconsiderando os ímpares')
if s == 0:
    print('Não tem números pares!')

#s não pode ser s = 0 + n pq s sempre vai ser 0
#s += n significa s+n é igual a S
