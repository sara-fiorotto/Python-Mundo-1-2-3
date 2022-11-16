n1 = int(input('Digite o primeiro número da PA:'))
r = int(input('Digite a razão da PA:'))
ultimo = 1
pa = n1 + r
print(pa, end=' ')
while ultimo <= 9:
    pa += r
    ultimo += 1
    print(pa, end=' ')



#for c in range(n1, decimo + r, r):
    #print('->', c, end=' ')