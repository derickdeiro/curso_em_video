import math
'''
Faça um progrmaa que leia um ângulo qualquer e mostre na tela o valor do
seno, cosseno e tangente desse ângulo.
No circulo o eixo vertical é do seno, o horizontal é do cosseno
'''

angulo = float(input('Digite o ângulo que deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(angulo, tangente))
