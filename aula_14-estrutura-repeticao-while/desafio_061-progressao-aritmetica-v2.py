"""
Refaça o DESAFIO 051, lendo o primeiro termo e a razao de uma PA, mostrando os 10
primeiros termos da progressao usando a estrutura while.
"""

primeiro = int(input('Primeiro termo: '))
razao = int(input('Digite em quantos números iremos contar: '))
cont = 1
termo = primeiro
while cont <= 10:
    print(termo, end=' - ')
    termo += razao
    cont += 1
print('ACABOU!')