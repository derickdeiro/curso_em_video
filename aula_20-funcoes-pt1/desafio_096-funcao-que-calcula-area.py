"""
Faça um programa que tenha um função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
"""


def área(larg, comp):
    a = larg * comp
    print(f'A área desse terreno retangular é {a:.0f}m².')


largura = float(input('Digite a largura do terreno (m): '))
comprimento = float(input('Digite o comprimento do terreno (m): '))
área(largura, comprimento)
