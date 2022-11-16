c = 0
s = 0
pare = 1
while pare != 999:
    n = int(input('Digite um número:'))
    if n != 999:
        c += 1
        s += n
    else:
        pare = 999
print(f'{c} Termos digitados e sua soma é {s}')




