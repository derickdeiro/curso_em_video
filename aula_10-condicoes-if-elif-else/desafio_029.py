'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada KM acima do limite.
'''

velocidade = float(input('Digite a velocidade que estava: '))


if velocidade > 80.0:
    print('MULTADO! Você excedeu o limite de velocidade que é 80km/h.')
    multa = (velocidade - 80.0) * 7
    print('O valor da multa é R$ {:.2f}.' .format(multa))
print()
print('Tenha um bom dia e dirija com segurança.')
