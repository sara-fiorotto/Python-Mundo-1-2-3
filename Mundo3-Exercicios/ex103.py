def ficha(nome='desconhecido', gols=0):
    if nome == '':
        nome = '<Desconhecido>'
    gols = int(gols)
    pontos = gols * 2
    print(f'O jogador {nome}, fez {gols} gols, e fez {pontos} pontos na Final')


jog = str(input('Nome do Jogador:'))
gol = str(input('Número de gols:'))
if gol == '':
    gol = 0
if jog == '':
    jog = '<Desconhecido>'

ficha(jog, gol)
