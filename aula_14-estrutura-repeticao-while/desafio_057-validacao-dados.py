"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valroes 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""


sexo = ''
masculino = 0
feminino = 0

while sexo != 'S':
    sexo = input('Qual seu sexo [M]asculino, [F]eminino? Sair = [S] ').strip().upper()[0]
    if sexo not in 'MmFfSs':
        print('Informação inválida. Tente novamente.')
    if sexo == 'M':
        masculino += 1
        print('Computado. Próximo.')
    if sexo == 'F':
        feminino += 1
        print('Computado. Próximo.')

print('Existem {} pessoas do sexo masculino e {} do sexo feminino.'.format(masculino, feminino))
