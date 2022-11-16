from time import sleep
print('VAMOS ÁS COMPRAS!!')
produto = float(input('Qual o valor do produto? R$'))
print('AS formas de pagamento disponíveis são DINHEIRO ,CHEQUE OU CARTÃO!!\n'
      'Lembrando que você pode parcelar as suas compras !\n'
      'Tecle (1) : para CARTÃO\n'
      'Tecle (2) : para DINHEIRO ou CHEQUE')
sleep(2)
pg = int(input('Qual vai ser a forma de pagamento?:'))
if pg == 1:
    cartao = int(input('Tecle (0) para pagamento á vista ou (1) para parcelado :'))
    if cartao == 0:
        print('Parabéns você ganhou 5% de desconto!')
        print('E você irá pagar R${} neste produto'.format(produto - (produto / 100 * 5)))
    elif cartao == 1:
        x = int(input('Quantas vezes você quer fazer:'))
        if x == 2:
            print('Você irá pagar duas parcelas de R${} (sem juros)'.format(produto / 2))
        if x > 2:
            juros = produto + (produto / 100 * 20)
            print('Você irá pagar JUROS ,agora o valor do produto é R${}'.format(juros))
            print(f'Você irá pagar {x} parcelas de {juros / x} ,desculpe o transtorno! ')
if pg == 2:
    print('PARABÉNS você ganhou 10% de desconto!')
    print('E você irá pagar apenas R${} neste produto!'.format(produto - (produto / 100 * 10)))
