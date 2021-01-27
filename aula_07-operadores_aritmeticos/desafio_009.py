'''
Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
'''

n1 = int(input('Qual tabuada deseja ver? '))

for i in range(11):
    res = n1 * i
    print('{} x {:2} = {}'.format(n1, i, res))
