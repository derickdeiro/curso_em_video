"""
Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

lista = []
for i in range(0, 5):
    numero = int(input('Digite um número: '))
    lista.append(numero)

print(f'Você digitou os números {lista}')
print(f'O maior valor foi {max(lista)} nas posições ', end='')
for pos, v in enumerate(lista):
    if v == max(lista):
        print(f'{pos}...', end='')
print()
print(f'O menor valor foi {min(lista)} nas posições ', end='')
for pos, v in enumerate(lista):
    if v == min(lista):
        print(f'{pos}...', end='')

print()
print('=*='*20)

listanum = []
maior = menor = 0
for i in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = listanum[i]
    else:
        if listanum[i] > maior:
            maior = listanum[i]
        if listanum[i] < menor:
            menor = listanum[i]
print(f'Você digitou os valores {listanum}')
print(f'O maior valor da lista é {maior} na posição... ', end='')
for pos, c in enumerate(listanum):
    if c == maior:
        print(f'{pos}...', end='')
print(f'O menor valor da lista é {menor} na posição... ', end='')
print()
for pos, c in enumerate(listanum):
    if c == menor:
        print(f'{pos}...', end='')
