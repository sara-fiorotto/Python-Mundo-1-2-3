contid = conthm = contml = 0
while True:
    print('CADASTRO DE PESSOAS')
    print('~~'*10)
    id = int(input('Idade:'))
    sx = str(input('Sexo: [M/F]')).upper()
    while sx not in 'MF':
        sx = str(input('Sexo: [M/F]')).upper()
    resp = str(input('Quer continuar: [S/N]')).upper()[0]
    if id > 18:
        contid += 1
    if sx in 'Mm':
        conthm += 1
    if sx in 'Ff' and id > 20:
        contml += 1
    if resp in 'N':
        break
    while resp not in 'S':
        resp = str(input('Quer continuar: [S/N]\n')).upper()[0]
print('------- ANALISANDO DADOS --------')
print(f'Ao todo tem {contid} pessoas com mais de 18 anos')
print(f'No progama tem {conthm} homens cadastrados')
print(f'Tem {contml} mulheres com mais de 20 anos.')