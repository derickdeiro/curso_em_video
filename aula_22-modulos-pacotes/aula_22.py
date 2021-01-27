import uteis  # ao utilizar esse modo, precisa utilizar uteis.fatorial (por exemplo)
# from uteis import fatorial, dobro, triplo  # não é recomendado devido a conflitos de importação


num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
# fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
# print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')
# print(f'O triplo de {num} é {triplo(num)}')
