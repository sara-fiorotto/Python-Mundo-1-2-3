c1 = s = maior = menor = 0
r = ''
while r != 'N':
    n = int(input('Digite um número'))
    s += n
    c1 += 1
    if c1 == 1:
        maior = n
        menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    r = str(input('Deseja continuar[S/N]:')).upper()
media = s / c1
print('O maior valor digitado é {} e o menor é {}, a media total é de {:.2f}'
      .format(maior, menor, media))
###parabéns , você conseguiu
###tem todo meu orgulho ai!