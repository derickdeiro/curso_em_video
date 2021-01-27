"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar.
No final, mostre:
- Qual é o total gasto na compra.
- Quantos produtos custam mais de R$ 1000.00
- Qual é o nome do produto mais barato.
"""

mais = soma = menor = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip().title()
    preço = float(input('Preço: R$ '))
    if soma == 0 or preço < menor:
        menor = preço
        barato = produto
    soma += preço
    if preço > 1000:
        mais += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
    print('---' * 15)
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto foi R$ \033[36m{soma:.2f}\033[m.')
print(f'{mais} produtos custaram mais do que R$ 1.000,00')
print(f'Dos produtos comprados, \033[32m{barato}\033[m foi o produto mais barato, custando R$ {menor:.2f}.')
