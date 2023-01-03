n1 = int(input('Digite um numero:'))
print('Tecle 1 para binario\n'
      'Tecle 2 para hexadecimal\n'
      'Tecle 3 para octa\n')
n2 = int(input('O que você gostaria de fazer?:'))
if n2 == 1:
    print(bin(n1)[2:])
elif n2 == 2:
    print(hex(n1)[2:])
elif n2 == 3:
    print(oct(n1)[2:])
else:
    print('Ops, acho que algo deu errado, tente de novo!')
