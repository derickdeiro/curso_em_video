"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função
input() do Python, só que fazendo a validação para aceitar apenas valor númérico.
Ex:
n = leiaInt('Digite um n')
"""


def leiaInt(msg):
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
    return f'Você digitou o número {numero}.'


numero = leiaInt('Digite um número: ')
print(numero)
