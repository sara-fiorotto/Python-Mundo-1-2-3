x = 0
while x != 5:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite um numero: '))
    print('[1] SOMA\n'
          '[2] MULTIPLICAR\n'
          '[3] MAIOR NÚMERO\n'
          '[4] DIGITAR NOVOS NÚMEROS\n'
          '[5] SAIR DO PROGAMA')
    resposta = int(input('O que vai fazer: '))
    if resposta == 1:
        print(f'A soma desses números é {n2 + n1}')
    if resposta == 2:
        print(f'A multiplicação desses números é {n2 * n1}')
    if resposta == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')
    if resposta == 4:
        print('Digite novos números!')
    if resposta == 5:
        x = 5
    if resposta > 5:
        print('Opção Inválida. Tente novamente ')
        resposta = 0
print('ACABOUU!')
