from time import sleep
"""
Escreva u programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário
ou então o empréstimo será negado.
"""

nome = input('Como se chama? ').strip()
nome = nome.title().split()
primeironome = nome[0]
casa = float(input('Certo \033[32m{}\033[m, qual o valor o imóvel que deseja comprar? R$ '.format(primeironome)))
anos = int(input('Perfeito \033[32m{}\033[m. Em quantos anos pretende pagar esse imóvel? '.format(primeironome)))
salario = float(input('E para concluírmos, qual o seu salário mensal? R$ '))
parcela = casa/(anos*12)
percentual = salario*30/100
print('=*='*6)
print('\033[33mANALISANDO...\033[m')
print('=*='*6)
sleep(0.5)

aprovado = 'PARABÉNS!!! Seu empréstimo foi {}aprovado{}, {}{}{}. Em alguns instantes o dinheiro estará em sua conta.'.format('\033[034m', '\033[m', '\033[032m', primeironome, '\033[m')
negado = 'Infelizmente seu empréstimo foi {}recusado{}, {}{}{}... Pedimos retome o contato em outro momento.'.format('\033[31m', '\033[m', '\033[032m', primeironome, '\033[m')
valor = 'O valor da parcela será de R$ \033[33m{:.2f}\033[m.'.format(parcela)

if parcela <= percentual:
    print(aprovado)
    print(valor)
else:
    print(negado)
print('Agradecemos o contato, tenha um bom dia.')
