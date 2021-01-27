"""
Crie um programa que tenha um função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e o outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo
de cálculo do fatorial.
"""


def fatorial(numero, show):
    from time import sleep
    produto = 1
    print(f'{numero}! ', end='')
    for i in range(numero, 0, -1):
        if show == 'S':
            print(f'{i} ', end='')
            sleep(0.5)
            if i > 1:
                print('x ', end='')
        produto *= i
    return f'= {produto}'


numero = int(input('Qual número deseja ver o fatorial? '))
show = str(input('Deseja exibir fatorial? [S/N] ')).strip().upper()[0]
print(fatorial(numero, show))

