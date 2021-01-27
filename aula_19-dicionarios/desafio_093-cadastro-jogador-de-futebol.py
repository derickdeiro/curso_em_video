"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
dados = dict()

dados['nome'] = str(input('Nome do Jogador: ')).strip().title()
qtd = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
dados['gols'] = list()
# soma = 0
for i in range(0, qtd):
    dados['gols'].append(int(input(f'Quantos gols na {i+1}ª partida? ')))
    # soma += dados['gols'][i]
# dados['total'] = soma
dados['total'] = sum(dados['gols'])  # 'sum' soma os dados dentro de uma lista.
print('-=-'*15)
print(dados)
print('-=-'*15)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-'*15)
print(f'O jogador {dados["nome"]} jogou {qtd} partidas.')
for pos, q in enumerate(dados['gols']):
    print(f'   => Na {pos+1}ª partida, fez {q} gols.')
print(f'Foi um total de {dados["total"]} gols.')
