from datetime import date
"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostar o tempo que falta ou que passou do prazo.
"""

ano = int(input('Digite o ano do seu nascimento: '))

idade = date.today().year - ano

if idade < 18:
    diferenca = 18 - idade
    print('Você tem {} anos, ainda \033[34mirá\033[m se alistar em {} anos.'.format(idade, diferenca))
elif idade == 18:
    print('Você já está com {} anos. \033[32mEstá na hora\033[m do alistamento. Boa sorte, soldado.'.format(idade))
else:
    diferenca = idade - 18
    print('Você está com {} anos! \033[31mPassou da hora\033[m do seu alistamento. '
          'Deveria ter feito isso à \033[33m{}\033[m anos.'.format(idade, diferenca))
