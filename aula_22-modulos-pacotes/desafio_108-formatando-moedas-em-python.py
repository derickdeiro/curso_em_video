import moeda
"""
Adapte o código do desafio 107, criando uma função adicional chamada
moeda() que consiga mostrar os valores como um valor monetário formatado.
"""

valor = float(input('Digite um valor: '))
p = float(input('Digite um percentual: '))
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O valor {moeda.moeda(valor)} com {p}% de desconto é {moeda.moeda(moeda.diminuir(valor, p))}')
print(f'O valor {moeda.moeda(valor)} com {p}% de aumento é {moeda.moeda(moeda.aumentar(valor, p))}')