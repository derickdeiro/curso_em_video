from random import randint
from time import sleep
'''
Escreva um programa que faça o ocmputador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu. 
'''
n1 = randint(0, 5)

num = int(input('Vou pensar em um número entre 0 e 5. Tente adivinhar... '))
print('PROCESSANDO...')
sleep(1)

if num == n1:
    print('ACERTOU! o número que estou pensando é {}.' .format(n1))
else:
    print('ERROU!!! O número que estava pensando era {} e não no {}.' .format(n1, num))
