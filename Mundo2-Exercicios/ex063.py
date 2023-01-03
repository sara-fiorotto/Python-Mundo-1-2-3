n1 = int(input('Quantos termos você quer ver?'))
t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end='')
c = 3
while c <= n1:
    t3 = t1 + t2
    print(t3, ' -> ', end='')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')
