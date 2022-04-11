"""
Crie um questionário perguntando nome e idade do usuário, trazendo uma resposta caso ele nao tenha mais que 18 anos, use coo exemplo se ele pode ou não fazer um empréstimo.

"""
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
idade_min = 18
idade_premium_inic = 20
idade_premium_final = 35

idade = int(idade)  #Como o input sempre resulta em uma string, preciso fazer type cast para transformar o valor em int

if idade >= idade_premium_inic and idade <= idade_premium_final:
    print(f'{nome}, você está com sorte, você tem a idade perfeita para um de nossos empréstimos Premium.')
elif idade >= idade_min:  #Não rolou fazer typecast direto aqui.. tive que converter antes nas variáveis.
    print(f'{nome}, você tem idade suficiente para solicitar um empréstimo padrão.')
else:
    print(f'{nome}, infelizmente você não tem idade suficiente para solicitar um empréstimo.')