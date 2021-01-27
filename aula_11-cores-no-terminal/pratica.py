a = 3
b = 5
print('Os valores são \033[33m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Derick'
cores = {'limpa': '\033[m', 
         'azul': '\033[34m',
         'amarelo': '\033[33m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!' .format(cores['azul'], nome, cores['limpa']))
