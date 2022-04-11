"""
ENTRADA DE DADOS usando o comando input

"""

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
ano_nasc = 2022 - int(idade)
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

print()
print(f'{nome} tem {idade} anos. '
    f'O {nome} nasceu em {ano_nasc}.')

print ()
print(f'A somatória entre os números que você informou é:')
print(int(num1)+int(num2))