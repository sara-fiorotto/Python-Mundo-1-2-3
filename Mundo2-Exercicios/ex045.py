from random import choice
jogo = ['PEDRA', 'PAPEL', 'TESOURA']
pc = (choice(jogo))
print('Bora brincar de Joken Pô?\n'
      'Vamos ver quem ganha !!\n'
      'TESOURA (1)\n'
      'PAPEL (2)\n'
      'PEDRA (3)\n')
pessoa = str(input('Pode começar: '))
print('o computador jogou', pc)
if pessoa == '1':
    print('Você jogou TESOURA')
elif pessoa == '2':
    print('Você jogou PAPEL')
else:
    print('Você jogou PEDRA')

if pc == 'PEDRA' and pessoa == '3' or pc == 'TESOURA' and pessoa == '1' or pc == 'PAPEL' and pessoa == '2':
    print('Eita ,empatou!!')
elif pc == 'TESOURA' and pessoa == '2' or pc == 'PEDRA' and pessoa == '1' or pc == 'PAPEL' and pessoa == '3':
    print('Você perdeu!!')
else:
    print('Você ganhou!!')
