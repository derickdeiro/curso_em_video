"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso mostre:
- Quantos números foram digitados.
- A lista de valores ordenada de forma decrescente.
- Se o valor 5 foi digitado e está ou não na lista.
"""
valores = []

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    print('Valor adicionado com sucesso.')
    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while escolha not in 'SsNn':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break

print(f'Foram digitados {len(valores)} elementos nesta lista.')
valores.sort(reverse=True)
print(f'A lista decrescente é {valores}')
if 5 in valores:
    print(f'O valor 5 foi encontrando nessa lista {valores.count(5)}x.')
else:
    print(f'O valor 5 não foi encontrado nessa lista.')
