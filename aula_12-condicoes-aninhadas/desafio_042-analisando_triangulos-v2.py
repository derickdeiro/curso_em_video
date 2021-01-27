"""
Refaça o desafio 035 dos triângulos, acescentando o recurso de mostrar que tipo
de triângulo será formado:
- Equilátero: Todos os lados iguais.
- Isósceles: dois lados iguais
- Escaleno: Todos os lados diferentes.
"""

a = float(input('Valor da primeira reta: '))
b = float(input('Valor da segunda reta: '))
c = float(input('Valor da terceira reta: '))




if a < b+c and b < a+c and c < a+b:
    print('As retas {:.1f}, {:.1f} e {:.1f} formam um triângulo '.format(a, b, c), end='')
    if a == b == c:
        print('\033[34mEquilátero\033[m.')
    elif a != b != c != a:
        print('\033[34mEscaleno\033[m.')
    else:
        print('\033[34mIsósceles\033[m.')
else:
    print('A retas {:.1f}, {:.1f} e {:.1f} \033[31mNÃO\033[m formam um triângulo.'.format(a, b, c))
