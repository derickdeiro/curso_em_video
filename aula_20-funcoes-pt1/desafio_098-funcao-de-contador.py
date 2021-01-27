from time import sleep
"""
Faça um programa que tenha um função chamada contador(), que receba três
parâmetros: início, fim e passo e realiza a contagem.
Seu programa tem que realizar três contagens através da função criada:
- De 1 até 10, de 1 em 1.
- de 10 até 0, de 2 em 2.
- uma contagem personalizada.
"""


def contador(ini, fim, passo):
    passoimpressao = passo
    if passo < 0:
        if fim > ini:
            troca = ini
            ini = fim
            fim = troca
        passoimpressao = passo * -1
    if passo == 0:
        passo = 1
        print(f'O intervalo não pode ser zero. Será considerado como 1.')

    print(f'O contador de \033[32m{ini}\033[m até \033[31m{fim}\033[m '
          f'indo de \033[33m{passoimpressao}\033[m em \033[33m{passoimpressao}\033[m é:', end=' ')
    sleep(1.5)

    if ini > fim:
        novofim = fim - 1
    if ini < fim:
        novofim = fim + 1

    for i in range(ini, novofim, passo):
        print(f'{i}', end=' ')
        sleep(0.5)
    print('FIM!')
    print('-'*75)


contador(1, 10, 1)
contador(10, 0, -2)
inicio = int(input('Começando com o número: '))
final = int(input('Terminando com o número: '))
intervalo = int(input('Com intervalo de: '))
contador(inicio, final, intervalo)


# SOLUCAO GUANABARA:
# def contador(i, f, p):
#     if p < 0:
#         p *= -1
#     if p == 0:
#         p = 1
#     print('-='*20)
#     print(f'Contagem de {i} até {f} de {p} em {p}:')
#     sleep(2.5)
#
#     if i < f:
#         cont = i
#         while cont <= f:
#             print(f'{cont}', end='')
#             sleep(0.5)
#             cont += p
#         print('FIM!')
#     else:
#         cont = i
#         while cont >= f:
#             print(f'{cont} ', end='')
#             sleep(0.5)
#             cont -= p
#         print('FIM!')
