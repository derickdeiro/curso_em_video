from time import sleep

"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro
de fogos de artificio, indo de 10 até 0, com pausa de 1 segundo entre eles.
"""

for i in range(10, -1, -1):
    print(i)
    sleep(0.5)
print('BUM! BUM! POOOW!!!')
