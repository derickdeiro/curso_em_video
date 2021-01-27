
"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""

def ano(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'Você tem {idade} anos de idade. Portanto', end=' ')
    if 16 <= idade < 18 or idade > 65:
        print(f'tem voto \033[34mFACULTATIVO\033[m.')
    elif idade < 18:
        print(f'você \033[31mNÃO VOTA\033[m.')
    else:
        print(f'tem voto \033[32mOBRIGATÓRIO\033[m.')


nascimento = int(input('Ano de nascimento: '))
ano(nascimento)
