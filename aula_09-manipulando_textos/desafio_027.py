'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.
EX: Ana Maria de Souza
primeiro = Ana
Último = Souza
'''

n = input('Digite seu nome completo: ').strip()
nome = n.split()

print('''
Seu primeiro nome é: {}
Seu último nome é: {}.'''.format(nome[0], nome[-1]))
