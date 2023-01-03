n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite mais um número: '))
lista = [n1, n2, n3]
if n1 != n2 or n1 != n3 or n2 != n3:
    print('o maior número é {}'.format(max(lista)))
    print('o menor número é {}'.format(min(lista)))
else:
    print('todos iguais')

#if n1 == n2 and n1 == n3 and n2 == n3:
#   print('Todos são iguais')
#else:
#   print('o maior número é {}!').format(max(lista)))
#   print('o menor número é {}!').format(min(lista)))
