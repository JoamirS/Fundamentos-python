with open('arquivo.txt', 'r') as arquivo:
    nome_string = arquivo.read().replace('\n', ', ')

print(nome_string)
