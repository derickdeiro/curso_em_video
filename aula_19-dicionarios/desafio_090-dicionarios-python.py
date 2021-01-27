"""
Faça um programa que leia o nome e média do aluno, guardando também a situação em um
dicionário. No final, mostre o conteúdo da estrutura na tela.
"""

alunos = {}
dados = []

while True:
    alunos['nome'] = str(input('Nome: ')).strip().title()
    alunos['media'] = float(input(f'Média do aluno {alunos["nome"]}: '))
    if alunos['media'] >= 7:
        alunos['situacao'] = '\033[34mAprovado\033[m'
    elif 5 <= alunos['media'] < 7:
        alunos['situacao'] = '\033[33mRecuperação\033[m'
    else:
        alunos['situacao'] = '\033[31mReprovado\033[m'
    dados.append(alunos.copy())
    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while escolha not in 'SsNn':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
# print(dados)
print('--'*15)
print(f'{"Cód.":<2} {"Aluno":<10} {"Situação":>10}')
print('--'*15)
for pos, info in enumerate(dados):
    print(f'{pos:<5}{info["nome"]:<12}{info["situacao"]:>8}')
