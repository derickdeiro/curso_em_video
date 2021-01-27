from random import randint
from time import sleep
from operator import itemgetter  # pega os itens pela ordem do dicionário
"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios (0, 6).
Guarde esses dados em um dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
EXEMPLO:
Jogador1 tirou 6
jogador2 tirou 2...
>> Ranking:
1º Lugar Jogador1 com 6...
2º Lugar jogadorX com Y...
"""
dados = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
sleep(1)
for k, v in dados.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)

print('-=-'*10)
print(f'{">>> RANKING <<<":^30}')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
