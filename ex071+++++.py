while True:
    print('\033[1;35m         Bem Vindo!!\n'
          '         Banco Saras\033[m')
    print(' $ '*10)
    vlr = int(input('Qual valor a ser sacado? R$ '))
    cinq = vlr // 50
    tira = vlr - (cinq * 50)
    vint = tira // 20
    tira2 = (vint * 20) + (cinq * 50)
    dez = (vlr - tira2) // 10
    tira3 = (vint * 20) + (cinq * 50) + (dez * 10)
    um = (vlr - tira3) // 1
    print('//' * 20)
    print(f'''    Total de {cinq} cédulas de R$50,00
    Total de {vint} cédulas de R$20,00
    Total de {dez} cédulas de R$ 10,00
    Total de {um} cédulas de R$1,00 ''')
    resp = str(input('Deseja sacar mais dinheiro? [S/N] ')).upper()[0]
    if resp in 'N':
        break
print('Obrigado ,Volte Sempre!')