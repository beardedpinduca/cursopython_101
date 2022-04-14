"""
Condições IF, ELIF, e ELSE
"""
print('EXEMPLO 1')
if True:  #espressão 'verdadeira' direta para exemplo.
    print('Esta espressão é verdadeira.')
else:
    print('Esta espressão não é verdadeira.')

print()
print('EXEMPLO 2')  #agora com 'várias' condições usando o elif, como se fosse um 'OU'
if False:
    print('Verdadeiro')
elif True:
    print('Agora e verdadeiro.')
elif False:
    print('Agora não é verdadeiro.')  #imprimiria tudo que estiver nesta hierarquia, leia-se abaixo deste elif e 4 'espaços'
    print('É impresso também pq está dentro da mesma hierarquia')
else:
    print('Não é verdadeiro.')