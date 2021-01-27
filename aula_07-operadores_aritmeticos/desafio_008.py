'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

n1 = float(input('Digite quantos metros tem o corredor: '))

cm = n1 * 100
mm = n1 * 1000

print('O corredor tem {:.2f} metros, que é o mesmo que {:.2f} centímetros e {:.2f} milímetros.'.format(n1, cm, mm))
