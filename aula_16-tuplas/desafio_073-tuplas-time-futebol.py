"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois Mostre:
- Apenas os 5 primeiros colocados.
- Os últimos 4 colocados da tabela.
- Uma lista com os times em ordem alfabética.
- Em que posição na tabela está o time do Bragantino.
"""

tabela = ('São Paulo', 'Internacional', 'Atlético-MG', 'Flamengo', 'Grêmio', 'Palmeiras',
          'Fluminense', 'Santos', 'Ceará SC', 'Corinthians', 'Athletico-PR',
          'Atlético-GO', 'Bragantino', 'Sport Recife', 'Vasco da Gama', 'Fortaleza',
          'Bahia', 'Goiás', 'Botafogo', 'Coritiba')

print('Os 5 primeiros colocados são: ', end='')
for i in tabela[0:5]:
    print(i, end=' / ')
print('\nOs últimos colocados são: ', end='')

for i in tabela[-4:]:
    print(i, end=' / ')
print('Os times em ordem alfabética ficam assim:')

for i in sorted(tabela):
    print(i, end=' ')

time = str(input('\nQual time deseja encontrar? ')).strip().title()
posicao = tabela.index(time)

print(f'O {time} está na {posicao+1}ª posição.')
