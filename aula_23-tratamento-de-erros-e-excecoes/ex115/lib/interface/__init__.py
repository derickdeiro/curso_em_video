def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Tivemos um problema com o valor que você digitou.\033[m')
        except KeyboardInterrupt:
             print(f'\033[31mERRO! O usuário preferiu não informar os dados.\033[m')
             return 0
        else:
            return numero

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção:\033[m ')
    return opc
