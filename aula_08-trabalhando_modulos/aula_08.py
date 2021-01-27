import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}.'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {:.2f}.'.format(num, raiz))

import random
num = random.randint(1, 100)
print(num)

