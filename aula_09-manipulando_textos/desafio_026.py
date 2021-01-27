'''
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.
'''

frase = input('Digite uma frase: ').lower().strip()
letra = input('Qual letra deseja procurar? ').lower()

print('A letra {} aparece {} vezes na frase.'.format(letra, frase.count(letra)))
print('Sendo a primeira na posição {} e última em {}.'.format(frase.find(letra)+1, frase.rfind(letra)+1))
