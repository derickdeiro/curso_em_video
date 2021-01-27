# help(input)  # é a ajuda interativa, basta colocar a função que deseja encontrar entre parenteses
# print(input.__doc__)  # mesma função que help()

#docstring é a documentação de uma função. É possível criar essa documentação conforme abaixo.
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela:  # param == parâmetro
    :param i: Início da contagem;
    :param f: Fim da contagem;
    :param p: Passo da contagem;
    :return: sem retorno.
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


contador(0, 10, 2)
help(contador)

# PARAMETROS OPCIONAIS
def somar(a=0, b=0, c=0):  # nesse caso, igualando o parâmetro a receber 0, não dá erro na função caso tenha menos
    s = a + b + c          # parâmetros que o informado.
    print(f'A soma vale {s}.')

somar(3, 2, 5)
somar(8, 4)
somar()
print('-=-'*30)
print()
def teste(b):
    a = 8
    b += 4  # b está valendo (a + b)
    c = 2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')


a = 5
teste(a)
print(f'A fora vale {a}.')
print('-=-'*30)
print()

def teste1(n2):
    global n1  # n1 está sendo substituida em todo o programa.
    n1 = 8
    n2 += 4  # b está valendo (a + b)
    n3 = 2
    print(f'N1 dentro vale {n1}.')
    print(f'N2 dentro vale {n2}.')
    print(f'N3 dentro vale {n3}.')


n1 = 5
teste1(n1)
print(f'N1 fora vale {n1}.')
print('-=-'*30)
print()

# RETORNANDO VALORES
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s  # retorna apenas o resultado como se fosse uma resposta para a função.


r1 = somar(3, 2, 5)
r2 = somar(8, 4)
r3 = somar()
print(f'As somas foram {r1}, {r2} e {r3}.')


