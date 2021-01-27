from random import randint
from time import sleep

"""
Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpite foram necessarios para vencer.
"""
print('''Olá, me chamo \033[35mALRAK\033[m e estou pensando em um número entre 0 e 10.
Tente adivinhar... =)''')
sleep(1)
print('Começando em:')
sleep(1)
for i in range(3, 0, -1):
    print('\033[33m{}\033[m'.format(i))
    sleep(1)
print('VALENDO!!!')
sleep(0.5)

computador = randint(0, 10)
acertou = False
contagem = 0

while not acertou:
    escolha = int(input('Digite um número: '))
    contagem += 1
    if escolha == computador:
        acertou = True
    else:
        print('\033[31mERRROOUU!\033[m')
        if escolha < computador:
            print('É um pouco mais...', end=' ')
        else:
            print('É um pouco menos...', end=' ')
        print('Tente novamente.')
print()
if contagem <= 1:
    palpite = '1 palpite'.format(contagem)
else:
    palpite = '{} palpites'.format(contagem)
print('Acertou!!! O número que estava pensando era \033[34m{}\033[m.'
      ' Precisou de \033[31m{}\033[m para você acertar.'.format(computador, palpite))
