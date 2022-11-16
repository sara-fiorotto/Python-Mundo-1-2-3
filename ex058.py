from random import choice
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n0 = choice(lista)
n1 = 0
soma = 0
acertou = False
print('Vamos brincar, qual número eu estou pensando? ...')
while n1 != n0:
    n1 = int(input('Digite um número de 0 a 10: '))
    if n1 != n0:
        soma += 1
        print('Ops, tente de novo!')
    if n1 < n0:
        print('Maior...')
    elif n1 > n0:
        print('Menor...')
if n1 == n0:
    print(f'Você acertou ,eu pensei em {n0}, você errou {soma} vezes')

# from random import randit
# sorteado = randit(0, 5)
# if sorteado == n1
