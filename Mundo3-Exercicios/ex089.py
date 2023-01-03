aluno = []
while True:
    nome = [str(input('Nome:'))]
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota2 + nota1) / 2
    notas = [nota1, nota2, media]
    nome.append(notas[:])
    aluno.append(nome[:])
    resp = str(input('Deseja continuar: [S/N]'))
    if resp in 'Nn':
        break
print('No. Nome      Média')
print('-'*25)
for pos, a in enumerate(aluno):
    print('{}    {:<10} {}'.format(pos, a[0], a[1][2]))
print('-'*25)
while True:
    q1 = int(input('Mostrar nota de qual aluno? [999 para!]'))
    if q1 == 999:
        break
    print('Notas de {}, são {} e {}'.
          format(aluno[q1][0], aluno[q1][1][0], aluno[q1][1][1]))
