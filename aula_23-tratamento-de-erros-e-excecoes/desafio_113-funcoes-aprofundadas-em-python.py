"""
Rescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
da digitação de um número de tipo inválido.
aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""

def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Tivemos um problema com o valor que você digitou.\033[m')
        except KeyboardInterrupt:
             print(f'\033[31mERRO! O usuário preferiu não informar os dados.\033[m')
             continue
        else:
            return f'Você digitou o número \033[33m{numero}\033[m.'


def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Tivemos um problema com o valor que você digitou.\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mERRO! O usuário preferiu não informar os dados.\033[m')
        else:
            # if numero.isnumeric():
            #     numero = float(numero)
            return f'Você digitou o número \033[33m{numero:.2f}\033[m.'


numero = leiaInt('Digite um número inteiro: ')
print(numero)
print('~' * 30)
real = leiaFloat('Digite um número real: ')
print(real)
