n1 = int(input('Digite o primeiro número da sua PA:'))
r = int(input('Digite a razão da sua PA: '))
decimo = n1 + (10 - 1) * r
for c in range(n1, decimo + r, r):
    print('->', c, end=' ')

#meu jeito
#s = n1 + r
#print(f'2º Termo :{s}')
#for c in range(3, 11):
    #s += r
    #print(f'{c}º Termo :{s}')

