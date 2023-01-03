def notas(*num, sit=False):
    """notas(*num, sit=False)
    -> Situação para avaliar os alunos de uma turma com vários resultados
    :param n: Recebe várias notas
    :param sit: Pode ser falso ou não, para mostrar a situação doa aluno de acordo com as notas
    :return: Retorna um dicionario com vários resultados que varia com a nota"""
    turma = {}
    x = 0
    turma['Total'] = len(num)
    turma['Maior'] = max(num)
    turma['Menor'] = min(num)
    for a in num:
        x += a
    turma['Media'] = x / turma['Total']

    if sit:
        if 8 > turma['Media'] > 5:
            sit = 'Vai passar'
        if turma['Media'] < 5:
            sit = 'Não vai passar'
        if turma['Media'] > 8:
            sit = 'Aluno Bom'
        turma['Situação'] = sit

    print(turma)


notas(5, 8, 6, sit=False)
help(notas)
