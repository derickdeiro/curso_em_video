"""
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando o laço for.
"""

num = int(input('Qual número deseja saber a tabuada? '))

for i in range(0, 11):
    print('{} x {:2} = {:2}'.format(num, i, num*i))
