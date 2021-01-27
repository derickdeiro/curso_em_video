from datetime import date
"""
Crie um programa leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
em um dicionário se por acaso o CTPS for diferente de ZERO,  o dicionário também receberá o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa irá se aposentar.
"""

dados = {}

dados['nome'] = str(input('Nome: ')).strip().title()
ano = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - ano
dados['ctps'] = int(input('Carteira de Trabalho (0 se não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratacao'] + 35) - date.today().year

for k, v in dados.items():
    print(f'{k} tem o valor {v}')
