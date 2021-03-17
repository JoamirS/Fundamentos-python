import re

default = "[0-9][a-z][0-9]"
text = "123 1a2 1cc aa1"
response = re.search(default, text)
print(response.group())
