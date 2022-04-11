"""
Quando quero 'deixar em branco' uma parte do código para continuar mais tarde, ou etc..
Podemos fazer isso de duas formas, usando o comando 'pass' ou 3 pontinhos '...' Exemplo abaixo:
"""
valor = True


# Bloco normal abaixo:
if valor:
    print('Olá')
else:
    print('Tchau')

# Bloco usando pass abaixo:
if valor:
    pass  #Isso faz com que o python desconsidere esta etapa.
else:
    print('Tchau')

# Bloco usando ... abaixo:
if valor:
    ...  #Isso faz com que o python desconsidere esta etapa.
else:
    print('Tchau')