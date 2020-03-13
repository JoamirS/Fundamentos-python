Snack = ('Hamburger', 'Lemonade', 'Pizza', 'Pudding')

'''
Tuplas são imutáveis.
Números negativos em uma posição, faz a contagem ser de trás para frente.
'''
# print(Snack)
# print(Snack[1])
# print(Snack[-2])
# print(Snack[1:3])
# print(Snack[-3:])

''' Utilizando a estrutura de controle for, podemos construir um contador para mostrar cada posição da tupla'''

# for meal in Snack:
#     print('Eu vou comer {}'.format(meal))
# print('Comi para caramba!')

''' Utlizando a estrutura de controle for, eu posso percorrer a minha tupla com o método len que pega o tamanho inteiro
da tupla. Pegando a cada posição da tupla pelo contador é posição mostrar todos os elemntos.
'''

# for CountTuple in range(0, len(Snack)):
#     print(f'Eu vou comer {Snack[CountTuple]}')

'''
    Juntamente com o comando enumerate é utlizado quando eu quero saber a posição do elemento na tupla e o seu nome.
'''
# for Position, TypesMeal in enumerate(Snack):
#     print(f'Hoje eu vou comer {TypesMeal} na posição {Position}')

''' A função sorted organiza a tupla em ordem alfabética '''
# print(sorted(Snack))

# NamesPeople = ('Joamir', 'Livramento', 'Gabriel', 'Carolina')
# print(sorted(NamesPeople))

''' Adicionando duas tuplas em uma terceira '''

TupleA = (2, 5, 4)
TupleB = (5, 8, 1, 2)

''' Note que o resultado das duas tuplas abaixo não são iguais, neste caso a ordem das parcelas alteram a soma.'''
TupleC = TupleB + TupleB
TupleD = TupleA + TupleB
print(TupleC)
print(TupleD)

'''count como o nome já diz, conta quantas vezes o elemento aparece na tupla'''
print(TupleC.count(5))

'''index mostra em qual posição está meu elemento, se estiver contido na tupla. Ele conta a partir da primeira 
    ocorrência'''
print(TupleC.index(2))

'''Caso queira procurar um elemento posterior a este, adicione uma vírgula e coloque o ponto que deseja iniciar'''
print(TupleC.index(2, 4))

'''del deleta a tupla'''
del TupleD
print(TupleD)
