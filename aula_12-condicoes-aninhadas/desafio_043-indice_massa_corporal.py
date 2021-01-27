"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre
seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso.
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórmida.
"""

peso = float(input('Qual o peso (kg)? '))
altura = float(input('Qual a altura (m)? '))
imc = peso/(altura**2)

if imc < 18.5:
    resultado = '\033[34mabaixo do peso\033[m'
elif 18.5 <= imc < 25:
    resultado = '\033[32mpeso ideal\033[m'
elif 25 <= imc < 30:
    resultado = '\033[33msobrepeso\033[m'
elif 30 <= imc < 40:
    resultado = '\033[31mobesidade\033[m'
else:
    resultado = '\033[35mobesidade mórbida\033[m, cuidado'
print('O IMC de {:.2f}, é considerado {}.'.format(imc, resultado))
