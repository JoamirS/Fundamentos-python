'''
    Listas em python.
    Uma lista em python é feita utlizando como parâmetro os colchetes no inicio e no fim. []

    A diferença entre append e extend é que o append adiciona a lista inteira em uma única posição e o extend separa
    cada item da lista em uma posição diferente.
'''

# Declarando a lista
ListA = ['c', 'a', 'l', 'l']

# Utlizando o método append para adicionar no final da lista
ListA.append('-')
ListA.append('m')
ListA.append('e')
ListA.append('!')
print(ListA)

# Fazendo a cópia da ListA
ListB = ListA.copy()
print(ListB)

# Contando quantas vezes aparece a letra 'l' em ListA
print(ListA.count('l'))
# ------------------------------------------------------------------------------------------------------------------

ListC = ['1', '2', '3']
ListD = ['um', 'dois', 'três']

# Adicionando o valor de ListD no final de ListC
ListC.extend(ListD)
print(ListC)

# Fazendo uma inserção na minha variável
ListC.insert(2, '23')
print(ListC)

# Removendo o último item da lista
ListC.pop()
print(ListC)

# Removendo o item que eu quero
ListC.remove('1')
print(ListC)

# Invertendo a ordem da lista
ListC.reverse()
print(ListC)

# Colocando os itens na ordem certa
ListE = ['4', '3', '7', '6', '1']
ListF = ['k', 'j', 'a', 'b', 'f']

ListE.sort()
ListF.sort()

print(ListE)
print(ListF)
