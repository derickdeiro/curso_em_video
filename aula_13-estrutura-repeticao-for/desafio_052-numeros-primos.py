"""
Faça um programa que leia um numero inteiro e diga se ele é ou não um número primo.
"""

num = int(input('Digite um número: '))
total = 0
for i in range(1, num+1):
    if num % i == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, total))
if total == 2:
    print('Por isso ele É PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO!')
