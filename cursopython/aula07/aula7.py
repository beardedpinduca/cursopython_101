"""
Uma maneira e formatar melhor as strings é usar f'', aí substitui as aspas por chaves {}
"""

nome = 'Jonas'
idade = 30
altura = 1.80
e_maior = idade>18
peso = 80
imc = peso/altura**2


print(nome, 'tem', idade, 'anos de idade e seu IMC é de', imc)  # esta é a maneira dificil...
print(f'{nome} tem {idade} anos de idade e seu IMC é de {imc:.2f}')  # esta é a maneira fácil... ainda adicionei :.2f para reduzir o numero de casas do float
print('{} tem {} anos de idade e seu IMC é de {:.2f}'.format(nome, idade, imc))  # esta é outra maneira tmb..
print('{0} tem {1} anos de idade e seu IMC é de {2:.2f}'.format(nome, idade, imc))  # esta é outra maneira tmb..
print('Eu tenho {1} anos de idade, meu nome é {0} e meu IMC é de {2:.2f}'.format(nome, idade, imc))  # esta é outra maneira tmb..
print('Eu tenho {i} anos de idade, meu nome é {n} e meu IMC é de {im:.2f}'.format(n=nome, i=idade, im=imc))  # esta é outra maneira tmb..