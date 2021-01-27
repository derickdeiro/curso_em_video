"""
Crie um programa leia vários números inteiros pelo teclado. No final da execução, mostre
a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa
deve perguntar ao usuario se ele quer ou não continuar a digitar valores.
"""

escolha = 'S'
soma = contagem = maior = menor = 0

while escolha != 'N':
    num = int(input('Digite um valor: '))
    soma += num
    contagem += 1
    if contagem == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

media = soma / contagem
print('O maior número entre os digitados foi {}. O menor foi {:.2f} e'
      ' a média entre todos os números foi {}.'.format(maior, menor, media))
