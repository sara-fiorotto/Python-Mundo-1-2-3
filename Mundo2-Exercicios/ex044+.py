print('VAMOS ÁS COMPRAS!!!')
produto = int(input('Qual o valor da sua comprar? R$'))
print('''ESCOLHA SUA FORMA DE PAGAMENTO:
(1) Dinheiro /Cheque
(2) Cartão á Vista
(3) Parcelado : Até 2X no cartão
(4) Parcelado : 3X ou mais''')
pg = int(input('Qual forma de pagamento você escolhe: '))
if pg == 1:
    total = produto - (produto / 100 * 10)
    print('Parabéns ,você ganhou 10% de desconto e pagará R${} neste produto'.format(total))
elif pg == 2:
    total = produto - (produto / 100 * 5)
    print('Parabéns você ganhou 5% de desconto e ira pagar R${} neste produto'.format(total))
elif pg == 3:
    total = produto
    print('Seu produto não teve alteração e você ira pagar duas parcelas de R${}'.format(produto / 2))
elif pg == 4:
    parcelas = int(input('Quantas parcelas você gostaria de fazer? '))
    total = produto + (produto / 100 * 20)
    print('Você irá pagar {}X de R${} '.format(parcelas, total / parcelas))
else:
    total = produto
    print('Opção {}INVALIDA{}, {}tente novamente !{}'.format('\033[1;30;45m', '\033[m', '\033[1;35m', '\033[m'))
print(f'Seu produto foi de R${produto} para R${total}')
