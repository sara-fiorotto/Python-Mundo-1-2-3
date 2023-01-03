from EX115.Cadastro.Cadastro_Usuario import cadastrar, salvar, printa
from time import sleep


while True:
    print('-' * 30)
    print(f'{"MENU PRINCIPAL":^30}')
    print('-' * 30)
    print('1 - Ver as pessoas cadastradas\n'
          '2 - Cadastrar nova pessoa\n'
          '3 - Sair do sistema\n')

    opcao = str(input('Opção: '))
    while True:
        if opcao == '1':
            printa('BD.txt')
            break
        if opcao == '2':
            cadastrar()
            salvar('BD.txt', 'a')
            sleep(2)
            break
        if opcao == '3':
            break
        else:
            print('Ops, Tivemos um problema, Digite 1,2 ou 3!')
            opcao = str(input('Opção: '))
    if opcao == '3':
        break
