'''
Faça um programa que leia um número inteiro e mostre na leta o sucessor e o seu antecessor.
'''

n1 = int(input('Digite um número: '))

ant = n1 - 1
suc = n1 + 1

print('Analisando o valor de {}, seu antecessor é {} e o sucessor é {}.'.format(n1, ant, suc))