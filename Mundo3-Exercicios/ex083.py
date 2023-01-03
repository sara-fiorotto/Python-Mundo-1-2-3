lista = list(input('Digite sua expressão:'))
contador = 0
for c in lista:
    if c == '(':
        contador += 1
    if c == ')':
        contador += 1
if contador % 2 == 0:
    print('Sua Expressão esta correta!')
else:
    print('Sua Expressão não é válida')