import math
'''
Faça um programa que leia o comprimento do cateto oposto do cateto adjacente de um
triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.

A soma da hipotenusa é a soma do quadrado dos catetos.
'''

co = float(input('Digite o valor do Cateto Oposto (|): '))
ca = float(input('Digite o valor do Cateto Adjacente(_): '))

hipot = co**2 + ca**2
hp = math.sqrt(hipot)
h1 = math.hypot(co, ca)

print('Os lados do triângulo retângulo são: {:.2f}cm, {:.2f}cm e {:.2f}cm.'.format(co, ca, hp))
print('A hipotenusa é {:.2f}cm.'.format(h1))
