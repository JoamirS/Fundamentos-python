argument = "www.bytebank.com/cambio?moedaorigem=real"

index = argument.find("=")
sub_string = argument[index + 1:]
print(sub_string)
