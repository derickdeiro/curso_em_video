from time import sleep
"""
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema
de visualização de detalhes do aproveitamento de cada jogador.
"""

dados = {}
geral = []

while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador? ')).strip().title()
    qtd = int(input('Quantas partidas ele jogou? '))
    dados['gols'] = list()
    for i in range(0, qtd):
        dados['gols'].append(int(input(f'Quantos gols na {i+1}ª partida? ')))
    dados['total'] = sum(dados['gols'])
    geral.append(dados.copy())
    while True:
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if escolha in 'SsNn':
            break
    if escolha == 'N':
        break
    print('---'*15)

print('=-='*15)
print(f'{"cod":<6}', end='')  # imprime o código alinhado a esquerda.
for i in dados.keys():
    print(f'{i:<15}', end='')  # imprime o título das Keys de maneira ordenada.
print()
print(f'---'*15)

for pos, i in enumerate(geral):
    print(f'{pos:<6}', end='')  # imprime o código na lista 'geral'
    for d in i.values():
        print(f'{str(d):<15}', end='')  # imprime os valores do dicionário de maneira ordenada.
    print()
print(f'---'*15)

while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca <= len(geral):
        print(f'--LEVANTAMENTO DO JOGADOR {geral[busca]["nome"]}:')
        for pos, i in enumerate(geral[busca]['gols']):
            print(f'  No jogo {pos+1} fez {i} gols.')
    else:
        while busca > len(geral):
            print(f'ERRO! Não existe jogador com código {busca}! Tente novamente... ')
            busca = int(input('Mostrar dados de qual jogador? '))
    while True:
        escolha = str(input('Buscar mais jogadores? [S/N] ')).strip().upper()
        if escolha in 'SsNn':
            break
    print('---'*15)
    if escolha == 'N':
        break
print(f'FINALIZANDO...')
sleep(1)
print(f'>>> VOLTE SEMPRE <<<')
