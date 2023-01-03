from random import choice
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno?'))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
sorteado = choice(lista)
print('O aluno sorteado foi {}'.format(sorteado))

#professor não explicou direito
#para criar lista basta colocar as variavéis dentro de chaves []

