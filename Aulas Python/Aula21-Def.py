def fatorial(num=1):  # Num é o parametro
    f = 1
    for c in range(num, 0, -1):  ##A variavel c dentro do intervalo do parametro Num até 0 de -1, assim C é uma
        # variavel constante e descrecente
        f *= c  # F irá multiplicar o valor de C e o seu resultuda será seu valor atual, assim quando C for 2 e F 20
        # 20 *= 2 o resultado dessa multiplicação será o valor de F tendo assim um fatorial
    return f


print(f'O fatorial de 5 é {fatorial(5)}')


# retornando o valor fatorial com o parametro 5


def par(n=0):
    if n % 2 == 0:
        return True   # Se o resto da divisão por 2 for igual a 0 então a sentença se torna verdadeira
    else:
        return False  # Se não se torna falsa


num = int(input('Digite um numero:'))

if par(num):   # Se a função Par de Num for verdadeira então escreva par se não escreva impar, se colocarmos um not
    # na frente então se a função Par de num NÃO FOR (not) o numéro é impar, tem vários jeitos de se fazer
    print('É par')
else:
    print('É impar')
