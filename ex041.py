from datetime import date
cores = {'azul': '\033[1;36m', 'roxo': '\033[1;35m',
         'limpa': '\033[m', 'amarelo': '\033[1;33m'}
print('Vamos olhar qual sua categoria em {}NATAÇÃO{}!!'.format(cores['azul'], cores['limpa']))
ano = int(input('Qual o seu ano de nascimento? '))
print('...' * 20)
idade = date.today().year - ano
print(f'Você tem {idade} anos')
print('Vamos ver sua {}CATEGORIA...{}'.format(cores['roxo'], cores['limpa']))
if 1 <= idade <= 9:
    print('Sua categoria é {}MIRIM{}'.format(cores['amarelo'], cores['limpa']))
elif 10 <= idade <= 14: #não precisa por maior que 10, pois se ele esta abaixo de 14, ja é menor que 10
    print('Sua categoria é {}INFANTIL{}'.format(cores['amarelo'], cores['limpa']))
elif 15 <= idade <= 20:
    print('Sua categoria é {}SENIOR{}'.format(cores['amarelo'], cores['limpa']))
else:
    print('Sua categoria é {}MASTER{}'.format(cores['amarelo'], cores['limpa']))
