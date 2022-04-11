"""
Faça um programa que pergunte a hora ao usuário e diga a saudação adequada, ex:
Bom dia: 0-11
Boa tarde: 12-17
Boa noite: 18-23
"""
hora = input('Por favor, informe que horas são: ')

if hora.isdigit():
    hora = int(hora)

    if hora >= 0 and hora <= 24:
        if hora >= 0 and hora <=11:
            print('Muito obrigado, tenha um BOM DIA!')
        elif hora >= 12 and hora <= 17:
            print('Muito obrigado, tenha uma BOA TARDE!')
        elif hora >= 18 and hora <= 24:
            print('Muito obrigado, tenha uma BOA NOITE!')
    else:
        print('Por favor, informe somente a hora exata e "cheia", de 0 à 24.')
else:
    print('Por favor, informe somente a hora exata e "cheia", por ex: 23, 15, 02, 3...')


##################### RESOLVIDO DE FORMA MAIS PRÁTICA PELO CURSO:
if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print('Horário deve estar entre 0 e 23.')
    else:
        if hora <= 11:
            print('Bom dia.')
        elif hora <= 17:
            print('Boa tarde.')
        else:
            print('Boa noite.')

else:
    print('Por favor, digite um horário entre 0 e 23.')