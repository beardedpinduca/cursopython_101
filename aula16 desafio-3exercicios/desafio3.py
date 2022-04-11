"""
Faça um programa que peça o primeiro nome do usuário,
Se o nome ter 4 ou menos letras: diga que o nome é curto.
Se tiver entre 5 e 6 letras: seu nome é normal.
Se for maior que 6: seu nome é grande.
"""

nome = input('Por favor, digite seu nome: ')
tam_nome = len(nome)

if tam_nome <= 4:
    print(f'Seu nome possui somente {tam_nome} letras, ele é curto ein?')
elif tam_nome <= 6:
    print(f'Seu nome possui {tam_nome} letras, ele tem um tamanho normal, graças a deus..')
else:
    print(f'Seu nome possui {tam_nome} letras, caramba é grande ein?')
