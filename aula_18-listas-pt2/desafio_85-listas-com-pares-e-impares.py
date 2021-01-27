"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""

numeros = [[], []]

for i in range(0, 7):
    num = int(input(f'Digite o {i+1}º número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados: {numeros[0]}')
print(f'Os valores ímpares digitados: {numeros[1]}')
