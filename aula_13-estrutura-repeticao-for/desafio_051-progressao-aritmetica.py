"""
Desenvolva um programa que leia o primeiro termo e a razao de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

primeiro = int(input('primeiro termo: '))
razao = int(input('Digite em quantos números iremos contar: '))
decimo = primeiro + (10-1) * razao
for i in range(primeiro, decimo, razao):
    print(i, end=' - ')
print('Acabou')

