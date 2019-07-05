'''
    Operadores de atribuição
'''
#  1ª forma de declarar uma variável
anyVariable = 10
#  2ª forma de declarar uma variável
moreEqual, lessEqual, equalMultiplication, equalDivision, equalModule = 9, 9, 9, 9, 9
# Para concatenar duas variáveis é preciso transformá-las em strings
print(str(equalMultiplication) + '-' + str(equalDivision))

# Fazendo com que as variáveis recebam novos valores, através de operações.
moreEqual += 1
lessEqual -= 1
equalDivision /= 1
equalMultiplication *= 1
equalModule %= 2

print('O valor da variável soma-um é {}'.format(moreEqual))
print('O valor da variável subtrai-um é {}'.format(lessEqual))
print('O valor da variável divide-um é {}'.format(equalDivision))
print('O valor da variável multiplica-um é {}'.format(equalMultiplication))
print('O valor da variável módulo-dois é {}'.format(equalModule))

# Podemos fazer operações ao declarar as variaveis
VariableOne, VariableTwo, VariableThree = 2, 4, 8
VariableOne, VariableTwo, VariableThree = VariableOne * 2, VariableOne + VariableTwo + VariableThree, \
                                          VariableOne * VariableTwo * VariableThree

print('O valor da primeira variável é {}'.format(VariableOne))
print('O valor da segunda variável é {}'.format(VariableTwo))
print('O valor da terceira variável é {}'.format(VariableThree))


