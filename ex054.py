from datetime import date
ano = date.today().year
s = 0
n = 0
for c in range(0, 7):
    id = int(input('Qual o ano de nacsimento: '))
    if ano - id > 21:
        s += 1
    else:
        n += 1
print(f'{s} pessoa(s) já são maior de idade,'
      f' {n} pessoa(s) ainda não são  maior de idade..')
