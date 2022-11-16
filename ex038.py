print('\033[33mVAMOS VER QUAL NÚMERO É MAIOR??\033[m')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número:'))
if n1 > n2:
    print(f'O {n1} é maior, é o primeiro valor')
elif n2 > n1:
    print(f'O {n2} é maior, o segundo valor maior!')
else:
    print('Não existe valor \033[32mMAIOR\033[m eles são iguais!!')

