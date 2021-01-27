"""
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e menor peso lidos.
"""

for i in range(0, 5):
    peso = float(input('Digite o peso da {}a pessoa: '.format(i+1)))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso >= maior:
            maior = peso
        if peso <= menor:
            menor = peso

print('O menor peso foi \033[34m{:.2f}\033[mkg e o maior peso foi \033[31m{:.2f}\033[mkg.'.format(menor, maior))
