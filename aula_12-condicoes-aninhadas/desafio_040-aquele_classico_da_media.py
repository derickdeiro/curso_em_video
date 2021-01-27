"""
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0:
REPROVADO
- Média entre 5.0 e 6.9:
RECUPERAÇÃO
- Média 7.0 ou superior:
APROVADO
"""

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2

print('Considerando as notas {:.2f}, {:.2f} e média final de {:.2f}.'.format(nota1, nota2, media))
if media < 5.0:
    resultado = '\033[31mREPROVADO\033[m'
elif 5.0 <= media < 6.9:
    resultado = 'de \033[33mRECUPERAÇÃO\033[m'
else:
    resultado = '\033[34mAPROVADO\033[m'
print('O aluno está {}.'.format(resultado))
