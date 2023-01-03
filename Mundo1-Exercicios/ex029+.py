km = int(input('Qual a sua velocidade?: '))
if km > 80:
    print('Você foi multado')
    vlr= (km % 80) * 7               #multa = (km - 80) * 7
    print('O Valor a pagar é R${}!'.format(vlr))
else:
    print('Boa viagem!')
print('Dirija com segurança')

#Orgulho do meu bêbê
