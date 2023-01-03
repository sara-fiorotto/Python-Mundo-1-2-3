from random import choice
lista = [1, 2, 3, 4, 5]
n0 = choice(lista)
n1 = int(input('Digite um número de 0 a 5: '))
print('Processando...')
if n1 == n0:
    print('Você venceu! Eu pensei em {}'.format(n0))
else:
    print('Você perdeu! Eu pensei em {}'.format(n0))

#from random import randit
#sorteado = randit(0, 5)
#if sorteado == n1