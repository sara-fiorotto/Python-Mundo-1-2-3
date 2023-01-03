nome = str(input('Qual o seu nome completo:')).strip()
print('Seu nome em maiúsculas é ', nome.upper())
print('Seu nome em minúsuclas é ', nome.lower())
n2 = nome.split()
n3 = ''.join(n2)
print('Seu nome tem {} letras!'.format(len(n3)))
print('Seu primeiro nome tem {} letras'.format(len(n2[0])))

#print('Seu nome tem {} letras!'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find('a')))
#resolução do professor
#eu não acredito que consegui fazer isso
