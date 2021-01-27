"""
Melhore o DESAFIO 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""

primeiro = int(input('Primeiro termo: '))
razao = int(input('Digite em quantos números iremos contar: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, end=' - ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))