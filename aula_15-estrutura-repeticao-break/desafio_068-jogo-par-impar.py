from random import randint
"""
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
"""
contador = 0
while True:
    computador = randint(0, 100)
    jogador = int(input('Diga um valor: '))
    resultado = computador + jogador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
    if resultado % 2 == 0:
        parouimpar = '\033[34mPar\033[m'
    else:
        parouimpar = '\033[31mÍmpar\033[m'
    print('---'*18)
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {resultado} é {parouimpar}.')
    print('---'*18)
    if escolha in 'Pp' and parouimpar == 'Par':
        print('Você GANHOU!\nVamos jogar novamente...')
        contador += 1
    elif escolha in 'Ii' and parouimpar == 'Ímpar':
        print('Você GANHOU!\nVamos jogar novamente...')
        contador += 1
    else:
        print('Você PERDEU!')
        break
    print()
print()
print(f'GAME OVER! Você venceu \033[33m{contador}\33[mx.')
