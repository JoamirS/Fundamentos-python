from extractArgumentUrl import extractArgument
url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar"
argument = extractArgument(url)
origin_currency, destiny_currency = argument.extract_argument()
print(destiny_currency, origin_currency)
print(argument)
