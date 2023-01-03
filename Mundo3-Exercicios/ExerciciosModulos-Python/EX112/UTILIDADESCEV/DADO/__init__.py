def Leiadinheiro(dindin):
    while True:
        try:
            valor = str(input(dindin))
            if valor.isnumeric():
                return float(valor)
            elif ',' in valor or '.' in valor:
                return float(valor.replace(',', '.'))
            else:
                print('Digite um valor válido')
        except ValueError:
            print('Digite um valor válido')
