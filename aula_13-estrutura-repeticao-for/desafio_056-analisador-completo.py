"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade d grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos.
"""

somaidade = 0
velho = 0
ultimaidade = 0
feminino = 0

for i in range(0, 4):
    print('~~~~~ {}ª PESSOA ~~~~~'.format(i+1))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    genero = int(input('Genero: [1] Masculino // [2] Feminino: '))
    somaidade += idade
    if idade >= ultimaidade and genero == 1:
        ultimaidade = idade
        velho = nome
    if genero == 2 and idade >= 20:
        feminino += 1

media = somaidade/4
print('A média de idade do grupo é: {:.2f}.'.format(media))
print('{} é o homem mais velho do grupo.'.format(velho))
if feminino <= 1:
    plural = 'Existe'
    mulher = 'mulher'
else:
    plural = 'Existem'
    mulher = 'mulheres'
print('{} {} {} que tem mais de 20 anos.'.format(plural, feminino, mulher))
