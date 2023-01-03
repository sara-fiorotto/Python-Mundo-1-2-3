from datetime import date
sexo = int(input('''Qual o seu sexo
[ 0 ] = Masculino
[ 1 ] = Fêminino
Escolha sua opção:'''))
if sexo == 0:
    ano = int(input('Qual seu ano de nascimento: '))
    idade = date.today().year - ano
    print(f'Você tem {idade} ano(s) de idade logo:')
    if idade > 18:
        print('Já passou da hora de se alistar!')
        print('Ja se passaram {} ano(s) que você se alistou'.format(idade - 18), end='')
        print(' e seu alistamento foi em {}'.format(date.today().year - (idade - 18)))
    elif idade < 18:
        print('Sua hora vai chegar!')
        print('falta só {} ano(s)'.format(18 - idade), end='')
        print(' e você ira se alistar em {}'.format((18 - idade) + date.today().year))
    else:
        print('Bora se alistar, Corre menino')
else:
    print('Não se preocupe ,você não precisa se alistar!')