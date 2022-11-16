s = 0
nh = ''
idh = 0
mulher = 0
for p in range(1, 5):
    print(f'-----{p}º PESSOA -----')
    nome = str(input('NOME: '))
    id = int(input('IDADE: '))
    sx = str(input('Sexo [F/M]: ')).strip().upper()
    s += id
    if p == 1 and sx == 'M':
        nh = nome
        idh = id
    if sx == 'M' and id > idh:
        nh = nome
        idh = id
    if sx == 'F' and id < 20:
        mulher += 1
print('A média de idade do Grupo é de {} anos'.format(s / 4))
print(f'A idade do Homem mais velho é {idh} e seu nome é {nh}')
print(f'Ao total são {mulher} mulheres com menos de 20 anos')
