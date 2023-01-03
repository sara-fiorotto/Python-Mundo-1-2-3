cadastro = []

nome = idade = banco = ''


def cadastrar():
    global nome, idade, cadastro
    print('-' * 30)
    print(f'{"NOVO CADASTRO":^30}')
    print('-' * 30)

    nome = input('NOME: ')
    while nome == '':
        print('ERRO, Por Favor digite seu nome!')
        nome = input('NOME: ')

    idade = input('Idade:')
    while not idade.isnumeric():
        print('ERRO, Digite um número válido')
        idade = input('Idade:')

    cadastro = [nome, ' ', idade, '\n']
    return cadastro


def salvar(txt, red):
    banco = open(txt, red)
    banco.writelines(cadastro)
    return banco


def printa(txt):
    cont = 0
    lista = open(txt, 'r')
    print('-' * 30)
    print(f'{"LISTA DE PESSOAS CADASTRADAS":^30}')
    print('-' * 30)
    print(lista.read())
    '''for c in lista:
        print(c, end='')
        cont += 1
        print(cont)'''
    print()
