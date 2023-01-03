def user(n):
    cpf = 0
    nome = ctt = tel = eqp = ''
    usuario = {}
    usuarios = []
    while True:
        try:
            cpf = int(input('Digite seu CPF:'))
        except (ValueError, TypeError):
            print('Inválido, tente novamente!')
        else:
            usuario['cpf'] = cpf
        nome = input('Digite seu nome completo:').strip()
        eqp = input('Nome da equipe:').strip()
        limite(nome, 40, 'Máxiomo de 40 caracters, Nome completo:')
        limite(eqp, 30, 'Maximo de 30 caracters, Equipe: ')
        ctt = input('Telefone [0] ou Rádio [1]:')
        while ctt not in '01' or ctt == '':
            print('Digite 0 para telefone ou 1 para Rádio!!')
            ctt = input('Telefone [0] ou Rádio [1]:')
        if ctt == '0':
            tel = input('Digite seu telefone:')
            ctt = 'Telefone'
            limite(tel, 9, 'Digite os 9 digitos do seu telefone:')
        elif ctt == '1':
            tel = input('Digite seu rádio:')
            ctt = 'Rádio'
            limite(tel, 8, 'Digite os 8 dígitos do seu rádio')
        turno = input('Turnos: Manhã [M], Tarde [T], Noite [N]:').strip().upper()[0]
        while turno not in 'MNT' or turno == "":
            turno = input('M para Manhã, T para Tarde e N para noite! Tente novamente! :').upper()[0]
        if turno == 'M':
            turno = 'Manhã'
        if turno == 'T':
            turno = 'Tarde'
        if turno == 'N':
            turno = 'Noite'
        usuario['Nome'] = nome[:40].title().strip()
        usuario[ctt] = tel.replace('-', '').strip()
        usuario['Equipe'] = eqp.strip()
        usuario['Turno'] = turno
        usuarios.append(usuario)
        usuario.clear()
        return usuario


def limite(var, lim, msg):
    while len(var) > lim or var == '':
        var = input(f'{msg}')
    if len(var) <= lim:
        return var


print(user(2))

