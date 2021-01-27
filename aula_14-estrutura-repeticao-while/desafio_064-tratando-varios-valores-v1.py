"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre
quantos números foram digitados e qual foi a soma entre eles.
(desconsiderando o flag -999-).
"""

n = cont = soma = 0
while n != 999:
    n = int(input('Digite um valor: '))
    if n != 999:
        soma += n
        cont += 1
print('Foram digitados {} números e a soma entre eles é {}.'.format(cont, soma))
