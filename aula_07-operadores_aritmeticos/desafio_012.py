'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

preco = float(input('Qual o preço do produto? R$ '))
desc = int(input('Qual o percentual de desconto? '))

desconto = preco * (desc/100)
novopreco = preco - desconto

print('O preço do produto com {}% de desconto é de R$ {:.2f}.'.format(desc, novopreco))