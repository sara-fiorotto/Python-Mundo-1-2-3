km = int(input('Qual a distância da sua viagem?: '))
if km <= 200:
    print('Você tem que pagar R${}'.format(km * 0.50))
else:
    print('Você tem que pagar R${}'.format(km * 0.45))
