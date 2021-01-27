"""
Creie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar. No final, mostre:
- Quantas pessoas tem mais de 18 anos.
- Quantos homens foram cadastrados.
- Quantas mulheres tem menos de 20 anos.
"""

maior = homens = mulheres = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
    escolha = ' '
    while escolha not in 'NS':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
    print('---'*15)
print()
print(f'Foram computadas {maior} pessoas maiores de idade.')
print(f'Dentre elas, {homens} são do sexo masculino.')
print(f'E desse total, temos {mulheres} mulheres menores de 20 anos.')

