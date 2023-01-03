nome = str(input('Qual o seu nome completo:')).strip()
divisor = nome.split()
n1 = divisor[0]
print('Seu primeiro nome é :{}'.format(n1))
print('Seu ultimo nome é: ', divisor[-1])

#print('Seu ultimo nome é {}'.format(divisor[len(divisor)-1]))
