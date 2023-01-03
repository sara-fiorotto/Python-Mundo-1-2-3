from math import hypot
catop = float(input('Qual o valor do cateto oposto?: '))
catad = float(input('Qual o valor do cateto adjacente? '))
hp = hypot(catop, catad)
print('O valor da sua hipotenusa é {:.2f}!'.format(hp))
