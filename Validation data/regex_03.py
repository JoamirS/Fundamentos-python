# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1
# {n}
# {min, max}
# ()+ [a-zA-Z0-9]+


import re

text = '''
João trouxe flores para sua amada namorada em 10 de janeiro de 1970,
maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'jo+ão+', text, flags=re.IGNORECASE))
print(re.sub(r'jo+ão+', 'Felipe', text, flags=re.IGNORECASE))
print(re.findall(r've{3}m{1,2}', text, flags=re.IGNORECASE))

''' 
O exemplo abaixo mostra como podemos usar procurar palavras distintas (uma com sufixo ou e outra sem) 
utilizando expressões regulares com uma mesma expressão. 
'''

text_two = 'João ama ser amado'
print(re.findall(r'ama[od]{0,2}', text_two, flags=re.IGNORECASE))
