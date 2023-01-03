from random import randint, choice

lista2 = []
par = []


def sortear(lst):
    para = 0
    while True:
        num1 = choice(lst)
        lista2.append(num1)
        num1 = 0
        para += 1
        if para == 5:
            break

def somapar(*num):
    for a in lista2:
        if a % 2 == 0:
            par.append(a)


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sortear(lista1)
somapar(lista2)
print(sum(par))
print(lista2)
