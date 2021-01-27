"""
Crie um programa que tenha uma tupla totalmente preenchida com um acontagem por
extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-la por extenso.
"""
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    posicao = int(input('Digite um número (Entre 0 e 20): '))
    while posicao > 20 or posicao < 0:
        posicao = int(input('Número inválido. Digite um número (Entre 0 e 20): '))
    print(f'Voê digitou o número \033[31m{tupla[posicao]}\033[m.')
    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while escolha not in 'NnSs':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha in 'nN':
        break

