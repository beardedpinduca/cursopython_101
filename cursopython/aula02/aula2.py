"""
# print (123456)
# print ('Jonas', 'Diedrich')
print('Jonas', 'Diedrich', sep='-', end=' e ')  # O sep se refere ao separador, ou seja, é para identificar como quero separar as informações dentro da função print.
print('Carolina', 'Schwingel', sep='-', end='')  # Já o end, se refere a como quero 'finalizar' a função, por padrão ela segue para uma nova linha, mas se colocar end = '' por exemplo, ela diz que a proxima ação deverá acontecer diretamente colada ao print anterior
"""
"""
Exercício: printar o CPF abaixo de maneira a usar a 'máscara' que ele possui, leia-se os pontos e traço.
CPF: 824.176.070-18
"""
#Reslução do exercício:
print(824,176,'070', sep='.', end='-')  # Note que o 070 eu tive que colocar com aspas, pois não é um número inteiro digamos..
print(18)
