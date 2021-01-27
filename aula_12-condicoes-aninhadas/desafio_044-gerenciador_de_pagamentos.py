"""
Elabore um programa que calcule o valro a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
- a vista: dinheiro/cheque: 10% de desconto
- a vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros.
"""
print('{:=^40}'.format(' LOJAS DEIRÓ '))

total = float(input('Total da compra: R$ '))
print('''Forma de pagamento:
 [1] Dinheiro
 [2] Cartão ''')
opcao = int(input('Qual sua opção: '))

if opcao == 1:
    valor = total - (total * 10 / 100)
    print('Você ganhou 10% de desconto. O total de R$ {:.2f} passou para R$ {:.2f}.'.format(total, valor))
elif opcao == 2:
    parcela = int(input('Quantas vezes: '))
    if parcela == 1:
        valor = total - (total*5/100)
        print('Você ganhou 5% de desconto. O total de R$ {:.2f} passou para R$ {:.2f}.'.format(total, valor))
    elif parcela == 2:
        parcelado = total/parcela
        print('A parcela desse valor será de R$ {:.2f} ao mês. O total a pagar é R$ {:.2f}.'.format(parcelado, total))
    elif parcela >= 3:
        valor = total + (total*20/100)
        parcelado = valor/parcela
        print('O total de R$ {:.2f} parcelado em {}x terá uma parcela'
              ' de R$ {:.2f} ao mês.'.format(total, parcela, parcelado))
        print('O valor final a pagar será de R$ {:.2f}.'.format(valor))
else:
   print('\033[31mOPÇÃO INCORRETA.\033[m')
