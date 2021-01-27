"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

lista = ('arroz', 'carne', 'playstation', 'nintendo', 'xbox')

for palavra in (lista):
    print(f'\nA palavra {palavra.lower()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')



