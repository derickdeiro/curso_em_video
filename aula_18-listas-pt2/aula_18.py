dados = list()
dados.append('Pedro')
dados.append(25)
print(dados)

pessoas = list()
pessoas.append(dados[:])  # cria uma cópia de uma lista dentro de outra lista. PESSOAS[dados[]]
conjunto = [['Pedro', 25], ['Maria', 19], ['João', 32]]  # 3 listas dentro de uma lista composta.
print(conjunto[0][0])  # 'Pedro'
print(conjunto[1][1])  # 19
print(conjunto[2][0])  # 'João'
print(conjunto[1])  # ['Maria', 19]

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('-'*30)
print()

grupo = list()
dado = list()
for i in range(0, 3):
    nome = str(input('Nome: ')).strip().title()
    dado.append(nome)
    dado.append(int(input('Idade: ')))
    grupo.append(dado[:])
    dado.clear()
print(grupo)

for pessoa in grupo:
    if pessoa[1] > 21:
        print(f'{pessoa[0]} é maior de idade. Tendo {pessoa[1]} anos.')
    else:
        print(f'{pessoa[0]} é menor de idade. Tendo {pessoa[1]} anos.')
