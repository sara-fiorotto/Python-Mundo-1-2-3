sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite seu sexo:')).upper()
    if sexo != 'F' and sexo != 'M':
        print('Tente novamente!')
print('fim')
