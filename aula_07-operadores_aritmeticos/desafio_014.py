'''
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para
Fahrenheit.
'''

c = float(input('Informe a temperatura em ºC: '))

f = (c * 9/5)+32

print('A temperatura de {}ºC corresponde a {}ºF!'.format(c, f))