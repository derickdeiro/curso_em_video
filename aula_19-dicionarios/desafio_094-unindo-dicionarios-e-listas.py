"""
Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
- Quantas pessoas foram cadastradas.
- A média de idade do grupo,
- Uma lista com todas as mulheres,
- Uma lista com todas as pessoas com idade acima da média.
"""
dados = {}
grupo = []
soma = 0

while True:
    dados['nome'] = str(input('Nome: ')).strip().title()
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print(f'Erro! Digite "M" ou "F"')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    grupo.append(dados.copy())
    dados.clear()
    while True:
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if escolha in 'SsNn':
            break
    if escolha == 'N':
        break
print('-=-'*15)
media = soma / len(grupo)

print(f'- O grupo tem {len(grupo)} pessoas;')
print(f'- A média de idade é de {media:.0f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for i in grupo:
    if i['sexo'] == 'F':
        print(i["nome"], end='; ')
print()
print(f'- Lista das pessoas que estão idade acima da média: ')
for i in grupo:
    if i['idade'] >= media:
        for k, v in i.items():
            print(f'{k} = {v};', end='')
        print()
