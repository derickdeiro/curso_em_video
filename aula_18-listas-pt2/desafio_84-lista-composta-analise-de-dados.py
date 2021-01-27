"""
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
- Quantas pessoas foram cadastradas.
- Uma listagem com as pessoas mais pesadas.
- Uma listagem com as pessoas mais leves.
"""

dados = []
info = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso: ')))
    if len(info) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    info.append(dados[:])
    dados.clear()
    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while escolha not in 'SsNn':
        escolha = str(input('Informação Inválida. Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('=*='*20)

print(f'Foram digitadas {len(info)} pessoas.')
print(f'O maior peso encontrado foi {maior:.2f}kg com ', end='')
for peso in info:
    if peso[1] == maior:
        print(f'{peso[0]}...', end='')
print()
print(f'O menor peso encontrado foi {menor:.2f}kg com ', end='')
for peso in info:
    if peso[1] == menor:
        print(f'{peso[0]}...', end='')
