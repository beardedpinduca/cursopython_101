"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s , d ou f)

> - ESQUERDA
< - DIREITA
^ - CENTRO
"""
nome = 'Jonas Diedrich'
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print(divisao)  #este resultado trará um número flutuante com várias casas decimais: 3,333333333...
print('{:.2f}'.format(divisao))  #este resultado trará o resultado já com somente 2 casas decimais aparecendo (opção usando o .format)
print(f'{divisao:.2f}')  # este resultado também trará o resultado com somente 2 casas decimais, opção usando 'f strings'

print(f'{num_2:0>10}')  #este resultado trará '9' zeros à esquerda do num_2, o '10' representa quantos caracteres deverá ter.
print(f'{num_2:x>10}')  #este resultado trará '9' x à esquerda do num_2, o '10' representa quantos caracteres deverá ter.
print(f'{num_2:x<10}')  #este resultado trará '9' x à direita do num_2, o '10' representa quantos caracteres deverá ter.
print(f'{num_2:x^11}')  #este resultado trará '10' x com o num_2 no centro, o '11' representa quantos caracteres deverá ter.

print(f'{num_2:x>10.2f}')  #este resultado trará '6' x à esquerda do num_2, um 'ponto' e também 2 casas decimais, o '10' representa quantos caracteres deverá ter.

print(f'{nome:x^50}')  #este resultado trará a string 'nome' no centro de 50 caracteres, sendo os demais 'x'.

print(nome.lower())  #tudo minúsculo
print(nome.upper())  #tudo maiúsculo
print(nome.title())  #primeiras letras maiúsculas

