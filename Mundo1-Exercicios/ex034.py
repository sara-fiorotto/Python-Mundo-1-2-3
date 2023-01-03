salario = float(input('Qual o seu sálario?'))
if salario > 1250:
    aumento = salario // 100 * 10
if salario <= 1250:
    aumento = salario // 100 * 15
print('Seu sálario agora será de R${}'.format(salario + aumento))
