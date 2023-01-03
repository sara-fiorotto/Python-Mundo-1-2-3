valores = list()
impares = list()
pares = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar :[S/N]')).upper()
    if resp in 'N':
        break
for c in valores:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print('A lista completa é :', valores)
print('A lista de pares é :', pares)
print('A lista de impares é :', impares)
