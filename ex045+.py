from random import randint
print(str('VAMOAS JOGAR JOKENPO'))
lista = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('''ESCOLHA UMA DAS OPÇÕES:
(0) PEDRA
(1) PAPEL
(2) TESOURA''')
vc = int(input('Qual a sua opção?'))
print('**' * 10)
if vc == 1 or vc == 0 or vc == 2:
    print('O Computador jogou {}!'.format(lista[pc]))
    print('Você jogou {}!!'.format(lista[vc]))
print('**' * 10)
#JEITO GIGANTE DO PROFESSOR

if vc == 0:
    if pc == 1:
        print('jogador ganhou!')
    elif pc == 2:
        print('computador ganhou!')
    else:
        print('Empatou')
elif vc == 1:
    if pc == 0:
        print('computador ganhou')
    elif pc == 2:
        print('jogador ganhou')
    else:
        print('empatou')
elif vc == 2:
    if pc == 0:
        print('jogador ganhou')
    elif pc == 1:
        print('computador ganhou')
    else:
        print('empatou')
if vc != 0 and vc !=1 and vc != 2:
    print(' JOGADA INVÁLIDA')

###MEU JEITO ERA MAIS FACIL PUSSOR!!!KKKKK
#if pc == 0 and vc == 1 or pc == 1 and vc == 2 or pc == 2 and vc == 0:
    #print('Você ganhou')
#elif vc == 0 and pc == 1 or vc == 1 and pc == 2 or vc == 2 and pc == 0:
    #print('o computador ganhou')
#else:
    #print('empatou!')