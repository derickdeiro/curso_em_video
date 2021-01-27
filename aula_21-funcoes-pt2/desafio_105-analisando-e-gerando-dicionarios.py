"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings da função.
"""


def notas(*notas, show=False):
    sala = dict()
    sala['total'] = len(notas)
    sala['maior'] = max(notas)
    sala['menor'] = min(notas)
    sala['média'] = sum(notas) / len(notas)
    if show:
        if sala['média'] > 7:
            sala['situação'] = 'BOA'
        elif 5 <= sala['média'] <= 7:
            sala['situação'] = 'REGULAR'
        else:
            sala['situação'] = 'RUIM'
    return sala


print(notas(7, 5, 4, 10, show=True))
