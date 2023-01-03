pessoa = {}
pessoas = []
somaid = 0
while True:
    pessoa['nome'] = str(input('Nome:'))
    pessoa['idade'] = int(input('Idade:'))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]:')).upper()
        if pessoa['sexo'] in 'FM':
            break
        print('ERRO, digita certo')
    pessoas.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar[S/N]:')).upper()
        if resp in 'SN':
            break
        print('ERRO, digita certo')
    if resp in 'Nn':
        break
print(f'- O Grupo tem {len(pessoas)} pessoas.')
for p in pessoas:
    for k, v in p.items():
        if k == 'idade':
            somaid += v
media = somaid / len(pessoas)
print('- A média de idade {:.2f} anos.'.format(media))
print('- As mulheres cadastradas foram :', end=' ')
for p in pessoas:
    for k, v in p.items():
        if k == 'sexo' and v == 'F':
            print(p['nome'], end=' ')
print('\n- Lista das pessoas com idade acima da média:')
for p in pessoas:
    for k, v in p.items():
        if k == 'idade' and v > media:
            print('nome ==', p['nome'], ';', 'idade == ', p['idade'],';', 'sexo ==', p['sexo'])
            print()
