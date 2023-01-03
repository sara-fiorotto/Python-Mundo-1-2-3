n1 = int(input('Digite um número:'))
x = 0
print(f'Esse número é divisivel por', end=':')
for c in range(1, n1+1):
    if n1 % c == 0:
        x += 1
        print(c, end='')
print(f'\n O número foi divisivel {x} vezes')
if x > 2:
    print('Numero composto')
else:
    print('Numero primo')



#if n1 % 2 != 0 and n1 % 3 != 0 and n1 % 5 != 0 and n1 % 11 != 0:
    #print('primo')
#else:
    #print('numero composto')
