# cada caracter representa um número começando em zero até...
frase = 'Curso em Vídeo Python'  # contém 21 caracteres.
print(frase[9])  # mostra a letra na posição []
print(frase[9:14])  # mostra os carecteres entre X até Y [X:Y]
print(frase[9:21:2])  # mostra os carecteres entre X até Y pulando de Z em Z [X:Y:Z]
print(frase[:14])  # começa do início e vai até 14 [0:14]
print(frase[9:])  # começa em 9 e vai até X [9:X]
print(frase[::3])  # vai do início até o fim pulando de x em x.

print(len(frase))  # conta o número de caracteres na string.
print(frase.count('o'))  # conta a quantidade do caracter entre ''. OBS: Maiúscula <> Minúscula.
print(frase.count('o', 0, 14))  # efetuando contagem já com fatiamento.
print(frase.find('deo'))  # encontrado a partir da contagem 14
print(frase.find('Android'))  # retornará '-1' significando que não existe dentro da string.
print('Curso' in frase)  # retorna booleano True ou False significando se existe ou não.
print(frase.replace('Python', 'Android'))  # adicionou a casa ao final e substituiu o que foi pedido.
print(frase.upper())  # troca as letras que estão em minúscula e coloca em maiúscula.
print(frase.lower())  # é o contrário de upper.
print(frase.capitalize())  # Deixa apenas a primeira letra maiúscula.
print(frase.title())  # coloca toda letra inicial em maiúscula.

frase2 = '   Aprenda Python  '  # frase com 3 espaços no inicio e dois no final.
print(frase2)
print(frase2.strip())  # remove o espaços do inicio e fim da frase.
print(frase2.rstrip())  # remove apenas os espaços da direita 'Right'.
print(frase2.lstrip())  # remove apenas os espaços da esquerda 'Left'.

print(frase.split())  # separa as frases pelo espaço, criando novas listas com cada uma delas.
                      # [Curso] [em] [Vídeo] [Python]
dividido = frase.split()
print(dividido[0])  # mostra a posição na lista dentro do split
print(dividido[0][3])  # mostra a letra na posição na lista dentro do split
print('-'.join(dividido))  # faz a junção das frases do 'split' com o separador que está '' antes do .join
