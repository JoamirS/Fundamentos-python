import re

email1 = "Meu número é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é o meu celular"
email4 = "lalalalalla 9423-1234 djfaksdjfsadkfhdkh 5654-4565 44445644"

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.findall(padrao, email4)
print(retorno)