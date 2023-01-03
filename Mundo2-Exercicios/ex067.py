while True:
    t = int(input('Qual tabuada você quer ver?'))
    if t < 0:
        break
    for tab in range(1, 11):
        print(f'{t} X {tab} = {t * tab}')
print('FIM, acabou a brincadeira!')
