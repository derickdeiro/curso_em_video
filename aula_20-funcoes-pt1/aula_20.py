def lin():  # cria uma função que é repetida quando chamada.
    print('-'*30)

lin()
print('Derick Deiró')
lin()


def mensagem(msg):  # irá retornar o que for escrito dentro dos parenteses
    print('-'*30)
    print(msg)
    print('-'*30)


mensagem('derick')


def soma(a, b):  # receberá apenas dois valores na função, A e B
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


soma(4, 5)
soma(b=4, a=2)


def contador(*num):  # o * recebe os valores digitados, DESEMPACOTA depois e cria uma Tupla
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

contador(1, 2, 6)
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [6, 3, 9, 1, 0, 2]
print(f'Os valores originais da lista são: {valores}')
def dobra(lst):  # pegará os valores que for indicado e dobrará o conteúdo de cada posição.
    pos = 0
    while pos < len(lst):  # enquanto a posição (pos) for menor do que o tamanho da lista, executa.
        lst[pos] *= 2  # lista (lst) na [posição] pos recebe ela vezes 2
        pos += 1  # pos recebe ele mais 1 para somar até chegar ao tamanho da lista.


dobra(valores)
print(f'Os valores dobrados da lista são: {valores}')

def somav(*numeros):  # DESEMPACOTAR para soma
    s = 0
    for i in numeros:
        s += i
    print(f'Somando os valores {numeros} temos {s}')

somav(1, 2)
somav(4, 3, 7)
