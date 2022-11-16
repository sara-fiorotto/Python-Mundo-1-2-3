total = mil = menorvalor = cont = 0
barato = ''
print('******LISTA DE COMPRAS******')
while True:
    print('-'*30)
    nome = str(input('Nome do Produto:'))
    valor = int(input('Valor do Produto: R$'))
    cont += 1
    total += valor
    if cont == 1 or menorvalor > valor:
        menorvalor = valor
        barato = nome
    if valor > 1000:
        mil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar: [S/N]')).upper()
    if resp == 'N':
        break
print('-'*30)
print('ANALISANDO COMPRA')
print(f'O total gasto na compra foi de R${total} em {cont} produtos')
print(f'Ao todo são {mil} produtos acima de R$1.000,00')
print(f'o produto mais barato é {barato} e custa R${menorvalor}')