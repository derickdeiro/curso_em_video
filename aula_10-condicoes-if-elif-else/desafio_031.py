'''
Desenvolva um programa que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens até 200KM e
R$ 0,45 para viagens mais longas.
'''

distancia = float(input('Qual a distância da viagem? '))
print('Você está prestes a fazer uma viagem de {:.2f}Km.'.format(distancia))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
# valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R$ {:.2f}.'.format(valor))
