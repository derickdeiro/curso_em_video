"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros
elementos de uma sequência de Fibonacci.
EX:
0 - 1 - 1 - 2 - 3 - 5 - 8
"""

termo = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
cont = 3

while cont <= termo:
    n3 = n1 + n2
    print(n3, end=' - ')
    n1 = n2
    n2 = n3
    cont += 1
print('FIM')
