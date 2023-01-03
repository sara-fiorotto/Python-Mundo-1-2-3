gols = []
soma = 0
aproveitamento = {'nome': str(input('Nome do jogador:'))}
jogos = int(input(f'Quantos jogos {aproveitamento["nome"]} jogou? '))
for c in range(0, jogos):
    gols.append(int(input(f'Quantos gols ele fez na partida {c}:')))
    soma += gols[c]
aproveitamento['gols'] = gols[:]
aproveitamento['total'] = soma
print('*' * 30)
print(aproveitamento)
print('*' * 30)
for k, v in aproveitamento.items():
    print('O campo', k, 'tem valor', v)
print('*' * 30)
print(f'O jogador {aproveitamento["nome"]} jogou {jogos} partidas:')
for pos, g in enumerate(gols):
    print(f'=> Na partida {pos}, fez {g} gols')
print(f'Foi um to tal de {soma} gols')