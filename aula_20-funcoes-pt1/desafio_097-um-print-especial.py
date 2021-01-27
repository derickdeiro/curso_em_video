"""
Faça um programa que tenha um função chamada escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável.
ex:
escreva('Olá, Mundo!')
saida:
---------------
  Olá, Mundo!
---------------
"""


def título(msg):
    tam = len(msg)+4
    print('~'*tam)
    print(f'  {msg}  ')
    print('~'*tam)


frase = str(input('Digite uma frase: ')).strip().upper()
título(frase)
