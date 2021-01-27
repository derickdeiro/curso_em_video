from utilidadescev import dado
from utilidadescev import moeda

"""
Dentro do pacote utilidades CeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
mas com uma validação de dados para aceitar apenas valores que sejam monetários.
"""

valor = dado.leiaDinheiro('Digite um preço: R$ ')
p = dado.leiaDinheiro('Digite um percentual: ')
moeda.resumo(valor, p)
