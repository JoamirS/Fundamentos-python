"""
    O recurso List Comprehension também permite utilizar condições para o preenchimento da lista.
    Considere o objetivo de inicializar uma lista com os números pares a partir de uma lista de números inteiros qualquer,
    por exemplo, os números 1,3,4,5,7,8,9.
    Para descobrir se um número é par, usamos a condição numero%2 == 0, que verifica se o resto de uma divisão por 2 é zero.
    O código abaixo usa um loop para inicializar a lista de pares.

    inteiros = [1,3,4,5,7,8,9]
    pares = []
    for numero in inteiros:
        if numero % 2 == 0:
            pares.append(numero)
    Pesquise como o podemos usar o List Comprehension para fazer o mesmo que o código acima
"""

integer = [1, 3, 4, 5, 7, 8, 9]
pair_numbers = [number for number in integer if number % 2 == 0]
print(pair_numbers)
