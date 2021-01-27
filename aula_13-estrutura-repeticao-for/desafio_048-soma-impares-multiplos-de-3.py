"""
Faça um programa que calcule a soma entre todos os números ímpares que
sao múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

soma = 0
cont = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        cont += 1
        soma += i
print('A soma de todos os {} valores ímpares múltiplos de 3 é \033[34m{}\033[m.'.format(cont, soma))
