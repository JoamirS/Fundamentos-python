import re

string_test = 'Este é um teste de expressões teste regulares.'

print(re.search(r'teste', string_test))
print(re.findall(r'teste', string_test))
print(re.sub(r'teste', 'ABCD', string_test))

regexp = re.compile(r'teste')
print(regexp.search(string_test))
print(regexp.findall(string_test))
print(regexp.sub('DEF', string_test))

