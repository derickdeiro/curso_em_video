"""
Crie um programa que crie ma matriz de dimensão 3x3 e preencha os valores
lidos pelo teclado.
No final, mostre na tela com a formatação correta.
"""
dados = []
matriz = []

for i in range(0, 3):
    for j in range(0, 3):
        dados.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
    matriz.append(dados[:])
    dados.clear()

print('=~='*11)
for linha in matriz:
    for coluna in range(0, 3):
        print(f'[{linha[coluna]:^5}]', end=' ')
    print()
print('=~=' * 11)
