nota1 = float(input('Qual a sua nota da prova?:'))
nota2 = float(input('Qual a sua nota de participação?:'))
media = (nota2 + nota1) / 2
print('A sua média é {:.1f}'.format(media))
if media < 5:
    print('Você reprovou')
elif 5 <= media <= 6.9:
    print('Você esta de recuperação')
elif media >= 7:
    print('Você foi aprovado')
