print('\033[1;30;42mVamos ver como esta sua saúde!!\033[m')
print('--' * 20)
peso = float(input('Qual o seu peso? :'))
alt = float(input('Qual sua altura?: '))
imc = peso / (alt ** 2)
print('..' * 20)
print('Seu imc é {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[1;33mVocê esta abaixo do peso\033[m')
elif 18 <= imc < 25:
    print('\033[1;32mVocê esta no seu peso ideal!!\033[m')
elif 25 <= imc < 30:
    print('\033[1;33mVocê esta com sobrepeso!\033[m')
elif 30 <= imc < 40:
    print('\033[1;31mVocê esta com obesidade!!\033[m')
elif imc >= 40:
    print('\033[1;31;40mVocê esta com obesidade morbida\033[m')
