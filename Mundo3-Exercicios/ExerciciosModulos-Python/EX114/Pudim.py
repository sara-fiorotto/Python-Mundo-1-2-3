import requests


try:
    pudim = requests.get('http://pudim.com.br/')
    if pudim:
        print('Pudim acessado com sucesso!')
except:
    print('Não consegui pegar o pudim!')