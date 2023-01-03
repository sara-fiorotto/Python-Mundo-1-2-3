valores = list()
while True:
    n = int(input('Digite um valor:'))
    if n not in valores:
        print('Vou adicionar a Lista... ')
        valores.append(n)
    else:
        print('Valor já adicionado, não vou colocar na lista..')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar: [S/N]')).upper()
    if resp in 'N':
        break
valores.sort()
print(valores)