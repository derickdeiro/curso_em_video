'''
Faça um algoritmo que leia o salário de um funcionário e mostre
seu novo salário com 15% de aumento.
'''

salario = float(input('Qual o salário atual? '))
aumento = int(input('Qual o percentual de aumento? '))

aum = salario * (aumento/100)
novosalario = salario + aum

print()
print('Salário antigo: {:.2f}\nAumento de {}%.\nAumento real: R$ {:.2f}\nSalário atual: R$ {:.2f}'.format(salario, aumento, aum, novosalario))