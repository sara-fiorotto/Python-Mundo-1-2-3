print('Vamos brincar, sera que você consegue formar um TRIÂNGULO?')
r1 = int(input('Digite um número:'))
r2 = int(input('Digite outro número:'))
r3 = int(input('Digite mais um número:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Isso forma um triangulo c: !!')
    if r1 == r2 and r1 == r3 and r2 == r3: #nao precisa r2 == r3 pq ele ja é igual a r3 r1 == r2 == r3
        print('Esse triângulo é EQUILÁTERO')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1: #usar else:
        print('Esse triangulo é ISÓSCELES')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Esse triangulo é ESCALENO')
else:
    print('Infelizmente não temos um triângulo :c')