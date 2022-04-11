"""
TIPOS DE DADOS PRIMITIVOS
str - string - textos 'Assim' ou "Assim"
int - inteiro - números que não tem ponto, ex: 1234, 0, -10, -82732873
float - real/ponto flutuante - número com decimais, ex: 10.59 ou 1.5 ou 0.56
bool - booleano/lógico - true ou false

"""
print('Assim', type('Assim'))
print(1234, type(1234))
print(10.59, type(10.59))
print(10==10, type(10==10))
print('Jonas'=='Jonas', type('Jonas'=='Jonas'))
print('################################################')
print('10', type('10'), type(int('10')))  # Esta segunda etapa que fiz no com o int, converteu a string '10' para um numero inteiro, mudando a caracteristica da linguagem, isso se chama 'type casting'

"""
EXERCÍCIO: Faça uma espécie de formulário, com nome, idade, altura e se vc é maior de idade ou não, desta forma você terá uma str, int, float e um bool como exemplo
"""
# RESOLUÇÃO DO EXERCÍCIO:

print('Qual o seu nome?')
print('Resposta:', end=' ')
print('Meu nome é Jonas Diedrich', type('Meu nome é Jonas Diedrich'))
print('Qual a sua idade?')
print('Resposta:', end=' ')
print('Eu tenho ', 30, ' anos', type(30))
print('Qual a sua altura?')
print('Resposta:', end=' ')
print('Eu tenho ', 1.80, 'm de altura', type(1.80))
print('Você é maior de idade?')
print('Resposta:', end=' ')
print(30 > 18, type(30>18))
