"""
COMO CONTAR CARACTERES
Funciona com strings e outros tipos, porém não com números int.
Usamos a função 'len()'
"""
usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type)

string1 = input('Digite algo: ')
string2 = input('Digite mais alguma coisa: ')

print(f'O número total de caracteres que você digitou é {len(string1)+len(string2)}.')

