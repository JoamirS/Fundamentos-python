''' FUNÇÕES II '''

""" Interactive Help """
# É possível obter ajuda através da função 'help()'. É necessario entrar no console do python para descobrir o que
# determinada função faz.
# Exemplo: >>> Help
#          help> Print | O python mostrará todas as funcionalidades desta função.
# Para sair, digite: quit

# Outra maneira de descobrir as funcionalidades, é colocar help na frente do meu parâmetro.
# Exemplo: help(print)

""" Doc Interno """
# É possível imprimir o doc interno por este comando:
# print(input.__doc__)

""" DocStrings """
def contador(i,f,p):
    """
    Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

""" ESCOPO DE VARIÁVEL """
''' Existem dois tipos de varáveis: com escopo local e global.
    Local funcionam apenas dentro a minha função. Já as com escopo global, funcionam no programa como um todo.
'''
def redeglobo(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
redeglobo(a)
print(f'A fora vale {a}')

""" RETORNO DE VALORES """
'''
    Neste caso, podemos retornar valores de uma só vez, isto é, em uma mesma linha usando o comando return.
    Podemos alocar os parâmetros passados para a função em uma variável, sendo assim possível retornar todas as variáveis
    em conjunto.
'''


def somar(A=0, B=0, C=0):
    sum = A + B + C
    return sum


SumOne = somar(3, 2, 5)
SumTwo = somar(3, 5)
SumThree = somar(6)

print(f'Os resultados foram {SumOne}, {SumTwo}, {SumThree}')
print('---')

def fatorial(number=1):
    f = 1
    for count in range(number, 0, -1):
        f *= count
    return f


n = int(input(f'Digite um número: '))
print(fatorial(n))

