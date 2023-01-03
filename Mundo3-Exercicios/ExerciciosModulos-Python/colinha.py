def limite(var, lim, msg):
    while len(var) > lim:
        var = input(f'{msg}')
    if len(var) <= lim:
        return var


num = [3, 6, 4, 1]
for n1, n2 in enumerate(num):
    print(n1, n2)
    print(n1+n2)



