gols = []
jogadores = []
soma = 0
while True:
    print('--'*20)
    aproveitamento = {'nome': str(input('Nome do jogador:'))}
    jogos = int(input(f'Quantos jogos {aproveitamento["nome"]} jogou? '))
    for c in range(0, jogos):
        gols.append(int(input(f'Quantos gols ele fez na partida {c}:')))
        soma += gols[c]
    aproveitamento['gols'] = gols[:]
    aproveitamento['total'] = soma
    jogadores.append(aproveitamento.copy())
    gols.clear()
    soma = 0
    resp = str(input('Deseja continuar [S/N]:'))
    if resp in 'Nn':
        break
print('***' * 10)
print('COD ', end='')
for i in aproveitamento.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--'*20)
while True:
    levantamento = int(input('Mostrar levantamento de qual jogador? '))
    if levantamento == 999:
        break
    if levantamento >= len(jogadores):
        print(f'ERRO, tente novamente , não tem {levantamento} ')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR: {jogadores[levantamento]["nome"]}:')
        for pos, j in enumerate(jogadores[levantamento]['gols']):
            print(f'- No jogo {pos} ele fez {j} gols')
print('VOLTE SEMPRE')