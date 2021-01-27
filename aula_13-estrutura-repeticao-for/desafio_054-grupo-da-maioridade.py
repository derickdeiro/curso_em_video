from datetime import date
"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
maiores.
"""

maiores = 0
menores = 0
atual = date.today().year
for i in range(0, 7):
    nascimento = int(input('Digite o ano de nascimento da {}a pessoa: '.format(i+1)))
    idade = atual - nascimento
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print('{} pessoas são \033[31mMAIORES\033[m idade e {} são \033[36mMENORES\033[m.'.format(maiores, menores))
