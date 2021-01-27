'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares
ela pode comprar.
Considere o dólar a = 3,27
'''

real = float(input('Quanto dinheiro tu tem na carteira? R$ '))
dolar = 3.27
conv = real / dolar

print('Com R$ {:.2f}, é possível converter para US$ {:.2f}.'.format(real, conv))
