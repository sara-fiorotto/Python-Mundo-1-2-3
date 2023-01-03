def Leita_Int(num):
    para = False
    while True:
        try:
            n = int(input(num))
            if type(n) == int:
                return n
            else:
                print('Digite um valor inteiro válido!!')
        except KeyboardInterrupt:
            print('O usuário desistiu do programa')
            return 0


def Leia_Float(num):
    try:
        while True:
            n = float(input(num))
            if type(n) == float:
                return n

    except KeyboardInterrupt:
        print('O usuário desistiu do programa')
        return 0
