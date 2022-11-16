f1 = str(input('digite uma frase: ')).strip().upper()
palavras = f1.split()
junto = ''.join(palavras)
inverso = ''
print(junto[2])
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
