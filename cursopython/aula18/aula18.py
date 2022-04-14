"""

Manipulando Strings
* String Indices
* Fatiamento de Strings [inicio:fim:passo]
* Funções built-in  len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

"""
#índice [012345678] -  indices positivos, cada um dos caracteres(letras/espaços) do texto abaixo são iguais a um indice.
texto = 'Python S2'
print(texto[3])  # vai imprimir a letra h.
print(texto[5])  # vai imprimir a letra n.

#índice -[987654321] - indices negativos, cada um dos caracteres(letras/espaços) do texto abaixo são iguais a um indice positivo.
texto =  'Python S2'

#exemplo, quero retirar a 'barra' do final da url
url = 'www.google.com.br/'
print(url[:-1])  #vai imprimir a url 'menos' o último indice, que é a barra neste exemplo.