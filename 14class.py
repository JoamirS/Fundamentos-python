""""" FUNÇÕES """
''' Exemplo de função: SOMA'''


def sumtwovalues(valueA, valueB):
    totalsum = valueA + valueB
    print('O valor da soma entre {} e {} é {}'.format(valueA, valueB, totalsum))


# Programa principal
sumtwovalues(4, 5)
sumtwovalues(4, 8)
sumtwovalues(6, 8)
print()

""" Eu posso explicitar quem são meu valores de entrada no programa principal, de modo que eu posso escolher a ordem 
deles no programa """


def sumtwovaluesdeclaration(valuesA, valuesB):
    print('O valor de A é {}. O valor de B é {}'.format(valuesA, valuesB))
    totalsum = valuesA + valuesB
    print('O valor da soma entre {} e {} é {}'.format(valuesA, valuesB, totalsum))


sumtwovaluesdeclaration(valuesA=4, valuesB=5)
sumtwovaluesdeclaration(valuesB=4, valuesA=5)
sumtwovaluesdeclaration(valuesB=7, valuesA=3)

''' O conceito de desempacotamento é importante, pois quando queremos passar vários valores, em quantidades diferentes
podemos desempacotar os valores, e o python aceita os valores passados. '''


def count(*number):
    for valor in number:
        print('{} '.format(valor), end='')
    print('FIM')


count(5, 7, 3, 4)
count(8, 4, 7)
count(4, 5, 7, 3, 5, 9)

''' Outro exemplo '''


def countvalues(* numbers):
    size = len(numbers)
    print('Recebi os valores {} e são ao todo {} números'.format(numbers, size))


countvalues(2, 4, 8)
countvalues(9, 0)
countvalues(11, 1, 8, 7, 9, 0)

''' Criando uma função para dobrar valores de uma lista '''


def double(list):
    position = 0
    while position < len(list):
        list[position] *= 2
        position += 1


values = [6, 3, 9, 1, 0, 2]
double(values)
print(values)

''' Criando uma função para desempacotar e somar '''


def sum(* values):
    sumvalues = 0
    for Numbers in values:
        sumvalues += Numbers
    print(f'Somando os valores {values} temos {sumvalues}')


sum(5, 2)
sum(2, 4, 6)
