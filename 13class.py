""" Dicionário
    São representados pelas chaves
"""

People = {'Nome': 'Peter', 'Idade': 27, 'Sexo': 'Masculino'}
print(People['Nome'])

print(People.keys())
print(People.values())
print(People.items())

# Mostrando as chaves através de um laço
for Keys in People.keys():
    print(Keys)

# Mostrando a chave e os valores através de um laço
for Keys, Values in People.items():
    print(f'{Keys} = {Values}')

# Alterando o dado de um dicionário
DictionaryCars = {'Modelo': 'HB20', 'Ano': 2015}
DictionaryCars['Ano'] = 2018
for Keys, Values in DictionaryCars.items():
    print(f'{Keys} = {Values}')

# Adicionando um novo elemento ao dicionário
DictionaryCars['Placa'] = 'RTX-2080'
print(DictionaryCars)

# Colocando um dicionário dentro de uma lista
StatesBrazil = []
StateOne = {'UF': 'Maranhão', 'Sigla': 'MA'}
StateTwo = {'UF': 'Ceará', 'Sigla': 'CE'}
StatesBrazil.append(StateOne)
StatesBrazil.append(StateTwo)
print(StatesBrazil)

# Colocando um dicionário dentro de uma lista com um laço
StateInput = dict()
CountryBrazil = list()
for Count in range(0, 3):
    StateInput['UF'] = str(input('Unidade Federativa: '))
    StateInput['Sigla'] = str(input('Sigla do Estado: '))
    CountryBrazil.append(StateInput.copy())
print(CountryBrazil)

# Percorrendo os elementos dentro de uma lista de dicionários
for Item in CountryBrazil:
    for Key, Value in Item.items():
        print('O campo {} tem o valor {}'.format(Key, Value))

