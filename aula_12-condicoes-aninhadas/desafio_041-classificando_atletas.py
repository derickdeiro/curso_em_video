from datetime import date
"""
A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um attleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 25: anos SÊNIOR
Acima: MASTER
"""
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = atual - nascimento

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    categoria = '\033[35mMIRIM\033[m'
elif idade <= 14:
    categoria = '\033[36mINFANTIL\033[m'
elif idade <=19:
    categoria = '\033[34mJUNIOR\033[m'
elif idade <= 25:
    categoria = '\033[32mSÊNIOR\033[m'
else:
    categoria = '\033[31mMASTER\033[m'

print('Sua categoria é {}.'.format(categoria))
