#forma 1 de fazer
print('\033[36;40mOlá Mundo!\033[m')
nome = str(input('Tudo bem, como posso te chamar? '))

#forma 2 de fazer:
print('Prazer em te conhecer {}{}{}'.format('\033[1;32m', nome, '\033[m',))

#forma 3 de fazer
cores = {'limpa': '\033[m',
         'azul': '\033[36m',
         'lilas': '\033[35m',
         'amarelo': '\033[33m'}
print('Você é {}MUITO{} legal {}Xuxu{}!!'
      .format(cores['azul'], cores['limpa'], cores['amarelo'], cores['limpa']))