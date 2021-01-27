"""
Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
"""

def acessarsite(site):
    import urllib
    import urllib.request
    site = f'http://www.{site}'
    try:
        urllib.request.urlopen(site)
    except:
        print(f'\033[31mERRO! Não conseguir acessar o site {site}.\033[m')
    else:
        print(f'Consegui acessar o {site} com sucesso.')
        print(site.read())


site = str(input('Digite um site: www.'))
acessarsite(site)
