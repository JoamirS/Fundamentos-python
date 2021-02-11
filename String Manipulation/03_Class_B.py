from Extrair import ExtratorArgumentoUrl

'''
url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"

argumento = "Rodrigo de Oliveira Siqueira"
#            0123456789 11  15
listaUrl = argumento.split("")
print(listUrl)
'''

url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"

argumento = ExtratorArgumentoUrl(url)
print(argumento)

