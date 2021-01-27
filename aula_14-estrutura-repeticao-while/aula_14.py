# for i in range(1, 10):
#     print(i)
# print('FIM')
#
# c = 1
# while c < 10:
#     print(c)
#     c += 1
# print('FIM')

n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))
