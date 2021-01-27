# dados = {}  # OU dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados)
print(dados['nome'])  # imprime a key 'nome'
print(dados['idade'])
dados['sexo'] = 'M'  # cria a key 'sexo' ao final do dicionário e preenche com 'M'
del dados['idade']  # apaga a key 'idade' e seu conteúdo completo.
print(dados)  # Dados sem a key 'idade'

filme = {'titulo': 'Star Wars',  # '{' pode ser aberta e podemos incluir seu conteúdo
        'ano': 1977,             # ao longo das linhas
        'diretor': 'George Lucas'
        }                       #  fechamos '}' aqui
print(filme.values())  # ao utilizar o método interno 'values()' exibe os "VALORES"
print(filme.keys())  # ao utilizar o método interno 'keys()' exibe as "CHAVES"
print(filme.items())  # exibe os ITENS

for key, value in filme.items():
    print(f'O {key} é {value}.')
locadora = []
locadora.append(filme)
print(locadora)
print(f'O filme {filme["titulo"]} foi dirigido por {filme["diretor"]}.')  # referenciar utilizando filme["x"]

filme['titulo'] = 'Mandalorian'  # substitui o que está no valor do dicionário por outra informação.
print(f'A série {filme["titulo"]} é do universo de {filme["diretor"]}')

brasil = []
estado = {}
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).strip()
    estado['sigla'] = str(input('Sigla do estado: ')).strip().upper()[:2]
    brasil.append(estado.copy())  # Cria uma cópia. Igual [:] da lista.

for e in brasil:  # Estou varrendo os estados (e) dentro da lista "Brasil"
    for v in e.values():  # Estou varrendo os valores (v) dentro dos estados (e.values)
        print(v, end=' ')
    print()
