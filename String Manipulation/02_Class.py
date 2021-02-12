argumento = "moedaorigem=real"
index = argumento.find("=")
sub_string = argumento[index + 1:]
print(sub_string)

argumento_dois = "moedaorigem=real"
lista_argumentos = argumento_dois.split("=")
print(lista_argumentos)