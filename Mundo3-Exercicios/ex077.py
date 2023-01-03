palavras = ('Amor', 'Caixa', 'Jardim', 'Lousa',
            'Cafe', 'Pilao', 'Campo', 'Brinco',
            'Caneca', 'Vidro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')