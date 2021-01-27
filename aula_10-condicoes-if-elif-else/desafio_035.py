"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.
Para construir um triângulo é necessário que a medida de qualquer
um dos lados seja menor que a soma das medidas dos outros dois e
maior que o valor absoluto da diferença entre essas medidas.
(b-c) < a < (b+c)
(a-c) < b < (a+c)
(a-b) < c < (a+b)
"""

a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('As retas {}, {} e {} formam um triângulo.'.format(a, b, c))
else:
    print('As retas não formam um triângulo.')
