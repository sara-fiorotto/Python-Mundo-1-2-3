def voto(nasc):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    if idade > 50:
        return 'Você está velho'
    else:
        return 'Você vai ficar velho'


x = int(input('Qual seu ano de Nascimento:'))
print(voto(x))
