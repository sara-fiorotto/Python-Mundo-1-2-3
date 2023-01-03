nome = str(input('Nome:'))
mda = float(input(f'Média de {nome}:'))
situ = ' '
if mda < 7:
    situ = 'Reprovado'
else:
    situ = 'Aprovado'
turma1 = {'aluno': nome, 'media': mda, 'passou': situ}
print('**' * 10)
print(f'Nome é: {turma1["aluno"]}')
print(f'Média é: {turma1["media"]}')
if situ == 'Aprovado':
    print(f'\033[1;32mSituação é: {turma1["passou"]}')
else:
    print(f'\033[1;31mSituação é: {turma1["passou"]}')
