from random import randint
"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
valor que estão na tupla.
"""

aleatorios = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

maior = 0
menor = 0
print(f'Os números aleatórios foram:', end=' ')
for pos, i in enumerate(aleatorios):
    print(i, end=' ')
    if pos == 0:
        maior = aleatorios[0]
        menor = aleatorios[0]
    else:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
print(f'\nO maior número gerado foi {maior}.')
print(f'o menor número gerado foi {menor}.')

print(f'O Maior valor sorteado foi {max(aleatorios)}.')
print(f'O Menor valor sorteado foi {min(aleatorios)}.')
