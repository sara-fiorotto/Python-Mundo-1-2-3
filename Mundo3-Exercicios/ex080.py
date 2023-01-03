valores = list()
maior = menor = 0
for c in range(0, 5):
    num = (int(input('Digite um valor:')))
    if c == 0:
        maior = menor = num
        valores.append(num)
        print('Adicionado ao final da lista')
    else:
        if num > valores[-1]:
            maior = num
            print('Valor adicionado no final da lista ')
            valores.append(num)
        if num < menor:
            menor = num
            print('Adicionado a posição 0 da lista')
            valores.insert(0, num)
        if maior > num > menor:
            if num > valores[1]:
                if num > valores[2]:
                    valores.insert(3, num)
                    print('Valor adicionado na posição 3')
                else:
                    valores.insert(2, num)
                    print('Valor adicionado na posição 2')
            else:
                print('Valor adicionado na posição 1')
                valores.insert(1, num)
print(valores)
