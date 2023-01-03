def voto(nasc):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc

    print(f'Você tem {idade} anos!')
    if 65 >= idade >= 18:
        print('SEU VOTO É OBRIGATÓRIO')
    elif idade < 16:
        print('VOCê AINDA NÃO VOTA')
    else:
        print('SEU VOTO É OPCIONAL')


id = int(input('Digite seu ano de nascimento:'))
voto(id)
