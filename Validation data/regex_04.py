# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1

import re

'''
Percorrendo Tags HTML para capturar palavras utilizando expressões expressões regulares.
'''


text = '''
<p> Frase  1</p> <p> Frase 2 </p> <p> Frase 3 </p> <div> Frase 1 </div>
'''

print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', text))
