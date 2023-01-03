n = str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece:', n.count('A'))
print('Ela se encontra primeiro no caracter:', n.find('A')+1)
print('Ela aparece pela ultima vez:', n.rfind('A')+1)


#n.find = lado esquerdo
#r.find = lado direitp