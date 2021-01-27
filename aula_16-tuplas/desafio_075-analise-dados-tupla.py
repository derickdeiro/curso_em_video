"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
- Quantas vezes apareceu o valor 9.
- Em que posição foi digitado o primeiro valor 3.
- Quais foram os números pares.
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

ordem = (n1, n2, n3, n4)
print(f'Você digitou os valores {ordem}')
print(f'O número 9 apareceu {ordem.count(9)} vezes.')
if 3 in ordem:
    print(f'O número 3 foi encontrando a primeira vez na {ordem.index(3)+1}ª posição.')
else:
    print(f'Não foi digitado nenhum valor 3.')
print(f'Os valores pares digitados foram: ', end='')
for i in ordem:
    if i % 2 == 0:
        print(i, end=' ')


