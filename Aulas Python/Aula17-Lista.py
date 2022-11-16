num = (2, 5, 9, 10)
# na tupla não conseguimos substituir seus valores
# num[2] = 7
# numa lista conseguimos modificar seus valores
num1 = [1, 3, 5, 11, 25]
num1[0] = 2  # neste caso a lista mudou seu segundo valor
num1.append(2)  # adicionando o valor 2 por ultimo na lista
num1.insert(3, 10)  # na terceira posição foi inserido o valor 10
num1.sort()  # organiza a ordem da lista
print(num1)
num1.pop()  # remove o ultimo valor da lista
num1.remove(2)  # vai eliminar apenas a primeira ocorrência do valor
print(num1)

valores = list()
for t in range(0, 3):
    valores.append(int(input('Digite um valor: ')))
print('fim')
for n, v in enumerate(valores):
    print(f'Na posição {n} temos o valor {v}')