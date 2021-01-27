'''
Faça um programa que leia a largura e a altura de uma parade em metros.
Calcule a sua área e a quantidade necessária para pintá-la.
Sabendo que cada litro de tinta pinta uma área de 2m².
'''

larg = float(input('Qual a largura da tua parede? '))
alt = float(input('Qual a altura da tua parede? '))

area = alt * larg
tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².'.format(larg, alt, area))
print('Para pintar essa parede, você precisa de {}l de tinta.'.format(tinta))


