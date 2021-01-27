from random import randint
from time import sleep
"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteio() e somapar(). A primeira função vai sortear 5 números e vai colocá-los dentro
da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela
função anterior.
"""

numeros = list()


def sorteio(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        lista.append(randint(0, 100))
        print(lista[cont], end=' ')
        sleep(0.5)
    print(f'PRONTO!')


def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}.')


sorteio(numeros)
somapar(numeros)
