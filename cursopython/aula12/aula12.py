"""
OPERADORES LÓGICOS
and
or
not
in
not in

"""

comparacao1 and comparacao2  # o 'and' checa se ambas as comparações são verdadeiras(true), aí retorna verdadeiro(true)
comparacao1 or comparacao2  # o 'or' checa se qualquer uma das duas comparações sao verdadeiras(true), aí retorna verdadeiro(true).

#######################################################

#o 'not' inverte completamente a comparação, ex:

a = 2
b = 3

#NORMAL:
if b>a:
    print('B é maior que A.')
else:
    print('A é maior que B.')
#Como resultado print trará B é maior que A.

#Usando NOT:
if not b>a:
    print('B é maior que A.')
else:
    print('A é maior que B.')
#Como resultado print trará A é maior que B.

###################################################

#Exemplos de 'in' e 'not in', para conferir se 'existe' dentro da espressão ou comparação..

nome: 'Jonas Diedrich'

if 'a' in nome:
    print('Existe a letra "a" no seu nome.')
else:
    print('Não existe esta letra no seu nome.')

if 'a' not in nome:
    print('Não existe a letra "a" no seu nome.')
else:
    print('Existe esta letra no seu nome.')


