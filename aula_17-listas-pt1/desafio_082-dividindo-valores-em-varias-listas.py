"""
Crie um programa para ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
principal = []

while True:
    principal.append(int(input('Digite um número: ')))
    escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while escolha not in 'SsnN':
        escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break

principal.sort()
par = []
impar = []
for i in principal:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'Sua lista principal é {principal}')
print(f'Lista de pares: {par}')
print(f'Lista de Ímpares: {impar}')
