"""
Aprimore o desafio anterior, mosrtando no final:
- A soma de todos os valores pares digitados;
- A soma dos valores da terceira coluna;
- o maior valor da segunda linha.
"""

dados = []
matriz = []
somapar = somacoluna = maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        dados.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
    matriz.append(dados[:])
    dados.clear()

print('=~='*11)
for linha in matriz:
    for coluna in range(0, 3):
        print(f'[{linha[coluna]:^5}]', end=' ')
        if linha[coluna] % 2 == 0:
            somapar += linha[coluna]
    print()
print('=~='*11)
print(f'A soma dos números pares totalizou {somapar}.')

for linha in matriz:
    for coluna in range(0, 3):
        if coluna == 2:
            somacoluna += linha[coluna]
# MESMA INFORMACAO DA SOLUCAO ACIMA:
# for linha in range(0, 3):
#     somacoluna += matriz[linha][2]
print(f'A soma da terceira coluna é {somacoluna}.')

for linha in matriz[1]:
    if linha == 0:
        maior = matriz[linha]
    else:
        if linha > maior:
            maior = linha
print(f'O maior valor encontrado na linha 2 foi {maior}.')
