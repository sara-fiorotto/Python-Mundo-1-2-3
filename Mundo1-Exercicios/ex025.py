nome = str(input('Qual seu nome completo:')).strip()
n1 = nome.upper().split()
print('Seu nome tem Silva?', 'SILVA' in n1)


#não precisava usar o split
#print('Seu nome tem Silva?', 'SILVA' in nome.upper())
