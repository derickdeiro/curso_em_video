import random
'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
# aluno = random.randint(1, 4)
#
# if aluno == 1:
#     aluno = 'Derick'
# elif aluno == 2:
#     aluno = 'Karla'
# elif aluno == 3:
#     aluno = 'Clara'
# else:
#     aluno = 'Stheffany'
#
# print('O aluno que apagará a lousa é {}.'.format(aluno))

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))
