import time
print('\033[1;34mVAMOS FECHAR NEGÓCIO!!\033[m')
print('---' * 20)
casa = float(input('Qual o valor da CASA que você gostaria de comprar?'))
salario = float(input('Qual o valor da sua RENDA?'))
periodo = float(input('Em quantos ANOS você quer quitar a casa?'))
print('///' * 20)
print('\033[4;33mVERIFICANDO\033[m')
time.sleep(2)
prestacao = casa / (periodo * 12)
limite = salario / 100 * 30
if prestacao >= limite:
    print('Seu empréstimo não foi APROVADO, o valor da sua prestação será R${:.2f}'.format(prestacao))
    print('Você {}NÃO{} pode comprar essa casa!'.format('\033[1;31m', '\033[m'))
else:
    print('Seu empréstimo foi {}APROVADO{}, o valor da sua prestação será R${:.2f}'.format('\033[1;32m',
                                                                                           '\033[m',
                                                                                           prestacao))
    print('Você {}PODE{} comprar esta casa!'.format('\033[1;32m', '\033[m'))
    print('\033[36mFicamos FELIZES de fechar negócio com você!!\033[m')
