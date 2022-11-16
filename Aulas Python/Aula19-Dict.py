''''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
pessoas['nome'] = 'Luisa'
pessoas['peso'] = 90
for k, v in pessoas.items():
    print(f'{k} == {v}')'''

brasil = list()
estado = dict()
for c in range(0, 3):
    estado['uf'] = str(input('Nome:'))
    estado['sigla'] = str(input('Sigla:'))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(k, v)
for e in brasil:
    for k, v in e.items():
        if k == 'uf':
            print(f'O estado {v} tem sigla', end=' ')
        if k in 'sigla':
            print(v)
    print()