'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
'''

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))

total = n1 + n2
media = total / 2

print('A nota final entre {} e {} é {} e a média do aluno é {}.'.format(n1, n2, total, media))
