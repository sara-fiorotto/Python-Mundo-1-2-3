a = input('Digite algo: ')
print('O tipo primitivo desse valor é {}\n '
      'Só tem espaços? {}\n'
      ' É um número? {}\n'
      ' É alfabético? {}\n'
      ' É alfanumérico? {}\n'
      ' É maiuscula? {}\n'
      ' É minuscula? {}\n'
      ' É capitalizada?{}\n'
      .format(type(a), a.isspace(), a.isnumeric(), a.isalpha(), a.isalnum(), a.isupper(), a.islower(), a.istitle()))
