def ajuda(f):
    print(help(f))


azul = \033[]
print('*' * 10)
print('SISTEMA DE AJUDA HELP')
print('*' * 10)
x = str(input('Função ou Biblioteca: '))
ajuda(x)
