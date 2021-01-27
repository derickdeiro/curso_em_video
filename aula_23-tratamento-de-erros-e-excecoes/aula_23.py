# try:  # tenta fazer a função abaixo
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a/b
# except:  # se houver um erro, tipo X / 0 = ERRO. GENÉRICO
#     print(f'Infelizmente tivemos um erro...')
# else:  # deu certo. (Opcional)
#     print(f'O resultado é {r:.1f}')
# finally:  # deu certo / falha (Opcional)
#     print(f'Volte sempre! Muito obrigado.')

print('~'*30)

try:  # tenta fazer a função abaixo
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print(f'Tivemos problemas com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print(f'Não é possível dividir um número por 0 (zero).')
except KeyboardInterrupt:
    print(f'O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:  # deu certo. (Opcional)
    print(f'O resultado é {r:.1f}')
finally:  # deu certo / falha (Opcional)
    print(f'Volte sempre! Muito obrigado.')
