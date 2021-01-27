lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[2:])
print(lanche[:2])
print(lanche)

for comida in lanche:
    print(f'Eu vou comer {comida}.')
print(f'Comi pra caramba.')
print()

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} (posição {cont}).')
print(f'Comi pra caramba.')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} (posição {pos}).')

print(lanche)
print(sorted(lanche)) #  deixa a Tupla em ordem alfabética. (Ordenado)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(a)
print(b)
print(c)

print(c.count(5)) #  conta quantas vezes (X) aparece dentro da Tupla.
print(c.index(8)) #  mostra em que posição está a primeira ocorrência de (X) dentro da Tupla.
print(c.index(8, 1)) #  busca (X) A PARTIR da posição Y (X, Y).
del(b) #  apaga a tupla
