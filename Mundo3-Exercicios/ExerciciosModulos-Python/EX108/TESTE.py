from EX108 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é '
      f'{moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentando(p, 10))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuindo(p,13))}')
