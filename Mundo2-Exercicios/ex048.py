s = 0
c = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        s = s + cont
        c = c + 1
print('Ao todo são {} valores e sua soma total é {}'.format(c, s))






#minha solução que só mostra a soma de todos os valores
#s = 0
#for c in range(1, 501):
    #if c % 2 == 1:
        #if c % 3 == 0:
            #s += c
#print(s)
