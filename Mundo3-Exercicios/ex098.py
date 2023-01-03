from time import sleep


def contador(inicio, passo, fim):
    if inicio > fim:
        for t in range(inicio, (fim - 1), -passo):
            print(f'{inicio} ', end='')
            inicio -= passo
        print('fim')
    elif fim > inicio:
        for t in range(inicio, fim+1, +passo):
            print(f'{inicio} ', end='')
            inicio += passo
        print('fim')


contador(inicio=10, passo=2, fim=0)
contador(inicio=1, passo=1, fim=10)

inc = int(input('INICIO:'))
fin = int(input('FIM:'))
pas = int(input('PASSO:'))
if inc < 0:
    inc *= -1
if inc == 0:
    inc = 1
contador(inc, pas, fin)
