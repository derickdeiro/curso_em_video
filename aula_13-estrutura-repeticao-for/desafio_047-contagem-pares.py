"""
Crie um programa que mostre na tela todos os números pares que estão entre 1 e 50.
"""

pares = 0
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')
        pares += 1
print()
print('A quantidade de números pares é \033[31m{}\033[m.'.format(pares))
