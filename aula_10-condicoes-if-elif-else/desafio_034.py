"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valro do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Qual é o salário do funcionário? R$ '))

if salario <= 1250:
    aumento = salario + (salario*15/100)
else:
    aumento = salario + (salario*10/100)

print('Quem ganhava R$ {:.2f}, passará a ganhar R$ {:.2f}.' .format(salario, aumento))
