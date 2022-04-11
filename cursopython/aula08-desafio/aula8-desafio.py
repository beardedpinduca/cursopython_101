"""
1) Criar variáveis para nome(str), idade(int), altura(float) e peso(float) de uma pessoa.
2) Criar uma variável com o ano atual(int)
3) Obter o ano de nascimento da pessoa
4) Obter o IMC da pessoa com 2 casas decimais
5) Exibir o texto conforme ex:
Luiz tem 32 anos, 1.8 de altura e pesa 80kg
O IMC de Luiz é 24.69.
Luiz nasceu em 1987.

"""

nome = 'Jonas'
idade = 30
altura = 1.80
peso = 80
imc = peso/altura**2
ano_atual = 2022
ano_nasc = ano_atual-idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nasc}.')