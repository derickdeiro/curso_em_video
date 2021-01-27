from random import randint
from time import sleep
"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
palpite = []
mega = []

print('=~='*10)
print(f'{" JOGOS MEGA SENA ":^30}')
print('=~='*10)

jogos = int(input('Quantos jogos deseja criar? '))
sleep(0.5)
print('\033[33m-='*3, f'SORTEANDO {jogos} JOGOS', '-='*3)
sleep(1)
for i in range(0, jogos):
    while len(palpite) < 6:
        num = randint(1, 60)
        if num not in palpite:
            palpite.append(num)
    palpite.sort()
    mega.append(palpite[:])
    palpite.clear()
    print(f'\033[m{i+1}º JOGO: {mega[i]}')
    sleep(0.5)

print('=~='*10)
print(f'\033[31m{" BOA SORTE ":^30}\033[m')
print('=~='*10)


