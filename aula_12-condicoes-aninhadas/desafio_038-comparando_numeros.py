"""
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
"""

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 == n2:
    print('Não existe valor \033[31mmaior\033[m, os dois são \033[34miguais\033[m.')
elif n1 > n2:
    print('O \033[36mprimeiro valor\033[m é o \033[31mmaior\033[m.')
else:
    print('O \033[36msegundo valor\033[m é o \033[31mmaior\033[m.')
