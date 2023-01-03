from datetime import date

nome = str(input('Nome:'))
nascimento = int(input('Ano de Nascimento:'))
carteira = int(input('Carteira de Trabalho (0 não tem):'))
idade = date.today().year - nascimento
trabalhador = {'nome': nome, 'idade': idade, 'ctps': carteira}
if carteira != 0:
    trabalhador = {'nome': nome, 'idade': idade, 'ctps': carteira,
                   'contratação': int(input("Ano de contratação:")),
                   'salario': float(input('Sálario: '))}
    aposentadoria = (trabalhador['contratação'] + 35) - nascimento
    trabalhador['aposentadoria'] = aposentadoria
    print('--' * 20)
    for k, v in trabalhador.items():
        print('-', k, 'tem valor', v)
if carteira == 0:
    print('--' * 20)
    for k, v in trabalhador.items():
        print('-', k, 'tem valor', v)
