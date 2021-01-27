from time import sleep
"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair
"""
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo valor: '))
escolha = 0

while escolha != 5:
    escolha = int(input('''Escolha uma das opções abaixo:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair 
O que deseja fazer? '''))

    if escolha == 1:
        resultado = n1 + n2
        print('A soma entre {:.2f} e {:.2f} é {:.2f}.'.format(n1, n2, resultado))
    elif escolha == 2:
        resultado = n1 * n2
        print('O produto de {:.2f} x {:.2f} é {:.2f}.'.format(n1, n2, resultado))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
            print('O número maior entre {:.2f} e {:.2f} é {:.2f}'.format(n1, n2, maior))
        else:
            maior = n2
            print('O número maior entre {:.2f} e {:.2f} é {:.2f}'.format(n1, n2, maior))
    elif escolha == 4:
        print('OK, vamos tentar novamente.')
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo valor: '))
    elif escolha == 5:
        print('Finalizando...')
        sleep(0.5)
    else:
        print('Escolha inválida...')
    print('=-='*13)

print('PROGRAMA ENCERRADO.')
