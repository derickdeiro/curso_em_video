'''
Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com o nome "SANTO".
'''

cidade = input('Digite o nome da cidade: ').strip()
cidade = cidade.upper()
primeiro = cidade.split()

if primeiro[0] == 'SANTO':
    print('A cidade começa com "Santo".')
else:
    print('A cidade NÃO começa com "Santo".')
