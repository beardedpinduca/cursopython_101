"""
Variáveis deverão iniciar com letras, pode contér números, para separar usamos _ , e ideal ser em letras mínusculas
O sinal de = atribui um valor a uma variável.
"""

nome = 'Jonas'
idade = 30
altura = 1.80
e_maior = idade>18
peso = 80
imc = peso/altura**2

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior de idade:', e_maior)
print('Seu peso é:', peso)
print('##########')

#Exercício: calcular o IMC da pessoa acima.
print(nome, 'tem', idade, 'anos de idade e seu IMC é de', imc)