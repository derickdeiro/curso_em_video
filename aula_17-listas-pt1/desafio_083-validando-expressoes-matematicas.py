"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta.
"""

# (a+b)*((a*b)/c)

expressao = input('Digite a expressão: ')
lista = list(expressao)

barra1 = lista.count('(')
barra2 = lista.count(')')
if barra1 == barra2:
    print(f'A expressão \033[33m{expressao}\033[m está \033[32mcorreta\033[m.')
else:
    print(f'A expressão \033[33m{expressao}\033[m está \033[31mincorreta\033[m.')

# pilha = []
# for simb in expressao:
#     if simb == '(':
#         pilha.append('(')
#     elif simb == ')':
#         if len(pilha) > 0:
#             pilha.pop()
#         else:
#             pilha.append(')')
#             break
# if len(pilha) == 0:
#     print('Sua expressão é válida')
# else:
#     print('Sua expressão está errada.')
