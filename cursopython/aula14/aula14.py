"""
Quero criar uma calculadora, assim como já fizemos no passado, mas COMO impedir que o usuário digite o que é preciso? Ex: se é uma calculadora, nao quero que ele digite um 'a' por exemplo, e sim, somente números.
Para isso, usaremos alguns métodos aplicados a strings: isnumeric, isdigit e isdecimal, tanto faz, mas tem pequenas diferenças.
Essas funções trarão True ou False se o informado é número e 'positivo'.
"""

num1 = input('Digite um número: ')  #Esta variável que o input trará do usuário resultará em uma string.
num2 = input('Digite outro número: ')  #Esta variável que o input trará do usuário resultará em uma string.

if num1.isdecimal() and num2.isdecimal():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não pude realizar esta conta, por gentileza informe somente números positivos.')

##################### Outra alternativa ao invés de IF e ELSE:

try:
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
except:
    print('Não pude realizar esta conta, por gentileza informe somente números positivos.')