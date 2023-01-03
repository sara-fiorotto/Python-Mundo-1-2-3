maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Qual o {p}º peso: KG'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior} KG e '
      f'o menor peso lido foi de {menor} KG ')
