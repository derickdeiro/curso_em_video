import moeda
"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade().
Faça também um programam que importe esse módulo e use algumas dessas funções.
"""

valor = int(input('Digite um valor: R$ '))
p = float(input('Digite um percentual: '))
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'O valor {valor} com {p}% de desconto é {moeda.diminuir(valor, p)}')
print(f'O valor {valor} com {p}% de aumento é {moeda.aumentar(valor, p)}')
