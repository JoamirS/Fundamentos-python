""" Módulos e pacotes """
def fatorial(number):
    fatorialNumber = 1
    """ No range, o python vai sempre do até o penúltimo número descrito, por isso soma-se a variável number com o 1
    """
    for factors in range(1, number + 1):
        fatorialNumber *= factors
    return fatorialNumber


inputNumber = int(input('Digite um valor: '))
resultFatorial = fatorial(inputNumber)
print(f'O fatorial de {inputNumber} é {resultFatorial}')
