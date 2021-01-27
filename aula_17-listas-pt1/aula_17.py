lanche = ['Hambúrger', 'Suco', 'Pizza', 'Pudim' ]
print(lanche)
lanche[3] = 'Sorvete'  # Substitui o item 'Pudim' por 'Sorvete'.
print(lanche)
lanche.append('Cookie')  # append inclui ao final da Lista o item.
print(lanche)
lanche.insert(0, 'Hot-dog')  # insert inclui na posição X (X, '') o item desejado, renumerando as keys.
print(lanche)
del lanche[3]  # irã remover o item na key 3.
lanche.pop(3)  # pop é utilizado para remover o último da lista.

if 'Pizza' in lanche:  # Só vai apagar o item pizza, se o mesmo estiver na lista.
    lanche.remove('Pizza')  # remove o item entre ( ), não importando a posição. Eliminando o primeiro encontrado.

valores = list(range(4, 11))  # Cria uma lista começando da numeração X e indo até Y-1 (X = 4, Y = 11)
print(valores)  # (4, 5, 6, 7, 8, 9, 10)

valores2 = [8, 2, 5, 4, 9, 3, 0]
print(valores2)
valores2.sort()  # deixa os itens em ordem crescente ou alfabética.
valores2.sort(reverse=True)  # os itens foram organizados e depois colocados ao contrário (reverse)
print(valores2)
print(len(valores2))

valores3 = []
# valores3.append(5)
# valores3.append(9)
# valores3.append(4)

for cont in range(0, 5):
    valores3.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores3):
    print(f'Na posição {c} encontrei o valor {v}')
print(f'Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a  # cria uma ligação entre as listas. Alterando ambas.
c = a[:]  # cria uma cópia da lista. Mantendo a separação delas.
c[2] = 8
print(f'Lista {a}')
print(f'Lista {b}')
print(f'Lista {c}')

