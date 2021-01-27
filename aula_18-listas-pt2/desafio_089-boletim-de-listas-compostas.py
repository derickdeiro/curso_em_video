"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma
lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente.
"""
dados = []
lista = []
while True:
    nome = str(input('Nome: ')).strip().title()
    dados.append(nome)
    nota1 = float(input('Primeira nota: '))
    dados.append(nota1)
    nota2 = float(input('Segunda nota: '))
    dados.append(nota2)
    media = (nota1 + nota2)/2
    dados.append(media)
    lista.append(dados[:])
    dados.clear()
    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while escolha not in 'SsNn':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print(lista)
print('=-'*15)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('--'*15)
for pos, aluno in enumerate(lista):
    print(f'{pos:<4}  {aluno[0]:<6}   {aluno[3]:>8.2f}')
print('--'*15)

while True:
    busca = int(input('Qual aluno deseja buscar? (999 interrompe): '))
    for pos, aluno in enumerate(lista):
        if pos == busca:
            print(f'\033[33m{aluno[0]}\033[m tirou média \033[34m{aluno[3]:.2f}\033[m')
            print(f'Suas notas foram: {aluno[1]:.2f} e {aluno[2]:.2f}')
            if aluno[3] >= 7:
                situacao = '\033[32mAPROVADO\033[m'
            else:
                situacao = '\033[31mREPROVADO\033[m'
            print(f'O resultado final é {situacao}')
            print('--'*15)
    # if busca <= len(lista)-1:
    #     print(f'\033[33m{lista[busca][0]}\033[m tirou média \033[34m{lista[busca][3]:.2f}\033[m.')
    #     print(f'Suas notas foram: {lista[busca][1]:.2f} e {lista[busca][2]:.2f}.')
    # if lista[busca][3] >= 7:
    #     situacao = '\033[32mAPROVADO\033[m'
    # else:
    #     situacao = '\033[31mREPROVADO\033[m'
    #     print(f'O resultado final é {situacao}.')
    #     print('--'*15)
    if busca == 999:
        print('FINALIZANDO...')
        break
print('<<< VOLTE SEMPRE >>>')
