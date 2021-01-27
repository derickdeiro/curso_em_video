'''
Crie um programa que leia o nome de uma pessoa e diga se tem "SILVA" no nome.
'''

nome = input('Digite seu nome completo: ').strip()
nome = nome.lower()

if 'silva' in nome:
    print('Existe "Silva" em seu nome.')
else:
    print('Não existe "Silva" no seu nome.')