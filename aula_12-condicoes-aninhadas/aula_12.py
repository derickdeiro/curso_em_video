"""
Condições aninhadas:
if, elif e else.
"""

nome = input('Qual o seu nome? ')
if nome == 'Karla':
    print('{} é o nome da minha namorada.'.format(nome))
elif nome in 'Stheffany, Carlos, Rosi':
    print('Uma pessoa da minha família se chama {}.'.format(nome))
elif nome == 'Geraldo' or nome == 'Filipe':
    print('{} é o nome de um dos meus melhores amigos.' .format(nome))
elif nome == 'Derick':
    print('{} é o nome do meu programador.'.format(nome))
else:
    print('Talvez eu conheça alguém que se chame {}.'.format(nome))
print('Tenha um bom dia, {}!'.format(nome))
