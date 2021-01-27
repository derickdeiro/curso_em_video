import moeda
"""
Modifique as funções que foram criadas no desafio 107 para que elas aceitem
um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela
função moeda(), desenvolvida no desafio 108.
"""

valor = float(input('Digite um valor: '))
p = float(input('Digite um percentual: '))
show = str(input('Exibir dados formatados? [S/N] ')).strip().upper()[0]
print(f'O dobro de {moeda.moeda(valor, show)} é {moeda.dobro(valor, show)}')
print(f'A metade de {moeda.moeda(valor, show)} é {moeda.metade(valor, show)}')
print(f'O valor {moeda.moeda(valor, show)} com {p}% de desconto é {moeda.diminuir(valor, p, show)}')
print(f'O valor {moeda.moeda(valor, show)} com {p}% de aumento é {moeda.aumentar(valor, p, show)}')
