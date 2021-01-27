import math

'''
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela
a sua porção inteira. Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
'''

num = float(input('Qual número deseja ver? '))

print('A parte inteira de {} é {}.'.format(num, math.trunc(num)))
print('A parte inteira de {} é {}.'.format(num, int(num)))


