def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


mylist = [1, 4, 5, 8, 9, 11, 13, 12]

newlist = [e for x in mylist if x % 2 == 1]
print(newlist)
