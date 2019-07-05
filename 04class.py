'''
    Estrutura de repetição com contador
'''

#   Declarando a variável como sendo o contador
IndexNumber = 0
#   Criando a estrutura de repetição com while. Enquanto o contador for menor que 10, mostre o valor do contador.
#   Mas caso o contador seja 5, ele não mostrará o valor.
#   E quando o contador chegar no 8, o programa para de ser executado.

while IndexNumber < 10:
    if IndexNumber == 5:
        IndexNumber += 1
        continue
    print(IndexNumber)
    IndexNumber += 1
    if IndexNumber == 8:
        IndexNumber += 1
        break
else:
    print('Fim do loop')
