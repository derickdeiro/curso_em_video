'''
Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
R$ 60.00 por dia e R$ 0.15 por Km rodado.
'''

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos KM rodados? '))
pago = (60 * dias) + (0.15 * km)

print('O total a pagar pelo período e KM rodado é de R$ {:.2f}.' .format(pago))


