
"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))

if n1 > n2 and n1 > n3:
    print('O maior número é {:.2f}.'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior número é {:.2f}.' . format(n2))
else:
    print('O maior número é {:.2f}.' .format(n3))

if n1 < n2 and n1 < n3:
    print('O menor número é {:.2f}.' .format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor número é {:.2f}.' .format(n2))
else:
    print('O menor número é {:.2f}.'. format(n3))
