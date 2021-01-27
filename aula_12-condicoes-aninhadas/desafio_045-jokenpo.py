from random import randint
from time import sleep
"""
Crie um programa que faça o computador jogar "Jokenpô" com você.
"""

print('''Suas opções: 
[0] Pedra
[1] Papel
[2] Tesoura: ''')

jogador = int(input('Qual a sua escolha? '))

tabela = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)

vitoria = 'Você \033[36mVENCEU!\033[m \033[33m{}\033[m ganha de' \
          ' \033[33m{}\033[m.\nBom jogo.'.format(tabela[jogador], tabela[computador])
derrota = 'Você \033[31mPERDEU!\033[m \033[33m{}\033[m ganha de' \
          ' \033[33m{}\033[m.\nBom jogo.'.format(tabela[computador], tabela[jogador])
empate = '\033[32mEMPATE!\033[m Nós dois jogamos ' \
         '\033[33m{}\033[m. Vamos de novo.' .format(tabela[computador])

print('\033[35mJO!!!')
sleep(0.3)
print('KEN!!!')
sleep(0.3)
print('PÔ\033[m')
sleep(0.3)

print('~'*30)
print('Computador jogou \033[33m{}\033[m.'.format(tabela[computador]))
print('Você jogou \033[33m{}\033[m.'.format(tabela[jogador]))
print('~'*30)

if computador == jogador:
    print(empate)
elif computador == 0 and jogador == 1:
    print(vitoria)
elif computador == 1 and jogador == 2:
    print(vitoria)
elif computador == 2 and jogador == 0:
    print(vitoria)
else:
    print(derrota)
