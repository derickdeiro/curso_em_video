from time import sleep
"""
Faça um programa que tenha um função chamada maior(), que receba vários parâmetros com
valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""


def maior(*num):
    print('-=-'*20)
    print(f'Analisando os valores passados...')
    sleep(1)
    maior = 0
    for pos, i in enumerate(num):
        if pos == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        print(f'{i}', end=' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
