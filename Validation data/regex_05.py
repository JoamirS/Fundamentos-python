'''
# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1

Para realizar a contagem dos grupos de parênteses dentro e acessá-los, é preciso contá-los a partir da abertura dos
parênteses.

() \1
() () \1 \2
(()) () \1 \2 \3

'''

import re

text = '''
<p> Frase 1</p> <p> Frase 2 </p> <p> Frase 3 </p> <div> Frase 1 </div>
'''

tags = re.findall(r'(<([pdiv]{1,3})>(.+?)<\/\2>)', text)

for tag in tags:
    one, two, three = tag
    print(one, two, three)
