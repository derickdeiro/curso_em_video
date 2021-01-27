'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

n1 = int(input('Digite um número: '))

db = n1 * 2
tp = n1 * 3
rq = float(n1) ** 0.5

print('O dobro de {} é {}.\nSeu triplo é {}.\nA raiz quadrada é {:.2f}.'.format(n1, db, tp, rq))
