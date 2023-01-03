valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar:[S/N]')).upper()
    if resp in 'N':
        break
print(f'{"ANALISANDO":-^30}')
print(f'Ao todo foram digitados {len(valores)} valores')
valores.sort(reverse=True)
print(f'A lista de valores em forma decrescente fica {valores}')
if 5 in valores:
    print(f'O valor 5 foi digitado na lista e esta na posição {valores.index(5)+1} ')
else:
    print('O valor 5 não foi digitado ')