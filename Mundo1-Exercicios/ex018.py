from math import tan, sin, cos, radians
angulo = int(input('Qual o valor do angulo: '))
print('O seno é {:.2f}, o seu consseno é {:.2f} e sua tangente é {:.2f}'.
      format(sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
