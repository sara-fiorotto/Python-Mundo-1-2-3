n1 = int(input('Digite o primeiro número da PA:'))
r = int(input('Digite a razão da PA:'))
ultimo = 1
pa = n1 + r
resp = 1
cont = 0
print(pa, end=' ')
while resp != 0:
    if ultimo <= 9:
        pa += r
        ultimo += 1
        print(pa, end=' ')
        cont += 1
    if ultimo > 9:
        resp = int(input('\nQuantos termos você quer adicionar? '))
        if resp != 0:
            ultimo -= resp
print(f'Finalizado com sucesso tem {cont+1} termos na tela')
