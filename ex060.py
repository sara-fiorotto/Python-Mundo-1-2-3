n1 = int(input('Digite um número: '))
fat = 1
i = 1
for f in range(n1, 0, -1):
    print(f, 'x' if f > 1 else ' = ', end=' ')
    fat *= f
print(fat)
while n1 > 0:
    print(n1, end=' ')
    i *= n1
    n1 -= 1
print('=', i)
#while i <= n1:
    #fat *= i
    #i += 1
    #print(fat)


#fac = factorial(n1)
#print(fac)
