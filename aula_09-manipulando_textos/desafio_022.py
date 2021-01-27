'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas;
- O nome com todas minúsculas;
- Quantas letras ao todo sem considerar espaços;
- Quantas letras tem o primeiro nome.
'''


nome = input('Digite seu nome completo: ').strip()

print('Seu nome todo em maiúscula é: {}.'.format(nome.upper()))
print('Seu nome todo em minúscula é: {}.'.format(nome.lower()))
semespaco = nome.replace(' ', '')
print('O nome sem espaços tem {} letras.' .format(len(semespaco)))
primeironome = nome.split()
print('O primeiro nome tem {} letras.' .format(len(primeironome[0])))
