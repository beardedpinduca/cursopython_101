"""
EXERCÍCIO
Criar uma conferencia de login e senha.
"""

usuario = input('Digite seu nome de Usuário: ')
senha = input('Digite sua Senha: ')

usuario_bd = 'jonas14'  #bd é para ser 'banco de dados'
senha_bd = '1234'

if usuario == usuario_bd and senha == senha_bd:
    print('Você está logado.')
else:
    print('Usuário ou senha incorreto.')

