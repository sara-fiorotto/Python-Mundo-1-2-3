from time import sleep
r1 = float(input('Primeira Reta:'))
r2 = float(input('Segunda Reta:'))
r3 = float(input('Terceira Reta:'))
print('*' * 40)
print('Vamos ver se você tem um triângulo com essas retas ...')
print('*' * 40)
sleep(4)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Você tem um triângulo!!!')
else:
    print('Você não tem um triângulo!!!')