i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Pulo: '))

for c in range(i, f+1, p):
    print(c)
print('Fim')

print()

n = int(input('Quantos valores deseja somar? '))

soma = 0
for i in range(0, n):
    s = int(input('Digite um valor: '))
    soma += s
print('A soma desses números resulta em {}.'.format(soma))
