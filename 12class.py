""" Criando uma lista composta """
#People = [['Bruce Wayne', 45], ['Steve Rodgers', 70], ['Peter Parker', 20], ['Superman', 40]]
#print(People[0][0])

""" Criando uma estrutura em que faço o cadastro de 3 pessoas e no final apago os dados de Data, mas os dados de People continuam """
People = list()
Data = list()
AllAdulthood = 0
AllMinority = 0

for FormPeople in range(0, 3):
    Data.append(str(input('Nome: ')))
    Data.append(int(input('Idade: ')))
    People.append(Data[:])  # Este comando gera uma cópia
    Data.clear()  # Este comando limpa os dados de Data após fazer uma cópia sua

for Person in People:
    if Person[1] >= 21:
        print(f'{Person[0]} é maior de idade.')
        AllAdulthood += 1
    else:
        print(f'{Person[0]} é menor de idade.')
        AllMinority += 1

print(f'Temos {AllAdulthood} maiores de idade e {AllMinority} menores de idade.')
