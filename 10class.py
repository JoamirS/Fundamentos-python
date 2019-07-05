'''
    Tuplas
        Pode-se armazenar dentro de uma tupla: numero, string e até outra tupla. Ela pode receber todos esses
        atributos de uma só vez.
'''

VariableA = ('a', 'b', 'c')
VariableB = ('a, b, c', 'c', 1, 2, 3)

# Contando quantas vezes a letra c aparece na tupla VariableB
print(VariableB.count('c'))

# Descobrindo em que posição está o elemento 'a' na tupla VariableA, se houver algum elemento 'a' na tupla.
if VariableA.count('a') > 0:
    print(VariableA.index('a'))

