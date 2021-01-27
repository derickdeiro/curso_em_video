"""
Faça um mini sistema que utilize o Interactive Help do Python. O usuário vai digitar
o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
OBS: Use cores.
"""
c = ('\033[m',   # 0 - sem cor
    '\033[31m',  # 1 - vermelho
    '\032[32m',  # 2 - verde
    '\033[33m',  # 3 - amarelo
    '\033[34m',  # 4 - azul
    '\033[35m',  # 5 - roxo
    '\033[36m',  # 6 - azul claro
);

def ajuda(cmd):
    help(cmd)


def título(msg, cor=0):
    tam = len(msg)+4
    print(f'{c[cor]}', end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(f'{c[0]}', end='')


comando = ''

while True:
    título('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Qual comando quer saber mais? '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 3)
