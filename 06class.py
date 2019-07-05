'''
    Estrutura de repetição For com a função zip
'''

ListOne = ['Macã', 'Banana', 'Melão']
ListTwo = ['Tomate', 'Cebola', 'Cenoura']

# O método zip faz com que as duas listas, sejam mostradas em pares lado a lado.

for IndexOne, IndexTwo in zip(ListOne, ListTwo):
    print(IndexOne, IndexTwo)

# O método enumerate faz a contagem dos elementos da lista, partindo sempre de 0.
# A variável IndexThree conta o número de elementos da lista e o IndexFour mostra o nome do elemento.
for IndexThree, IndexFour in enumerate(ListOne):
    print(IndexThree, IndexFour)

