import re

default = "[0-9][a-z][0-9]"
text = "123 1a2 1cc aa1"
response = re.search(default, text)
print(response.group())


default_two = "\w{5, 50}@\w{3, 10}.\w{2,3}.\w{2,3}"
text_two = "mdjskafk joamir123@gmail.com.br dflksls dfosdk"
response_two = re.search(default_two, text_two)
print(response_two.group())
