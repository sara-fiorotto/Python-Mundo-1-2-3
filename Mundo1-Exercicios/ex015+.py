km = float(input('Quantos KM você rodou? '))
dia = float(input('Quantos dias você ficou com o carro? '))
vl1 = km * 0.15
vl2 = dia * 60
total = vl1 + vl2
print('Você tem que pagar R${}'.format(total))

#outra forma mais pratica de fazer
#pago = (km * 0.15) + (dia * 60)

