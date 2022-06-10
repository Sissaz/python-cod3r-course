# Desafio IBGE 

# Extrair o nono e o quarto campos do arquivo CSV sobre Região de influência das Cidades do IBGE. 

# Ignorando a primeira linha que é o cabeçalho

import csv
import imp
from urllib import request

def read(url):
    with request.urlopen(url) as entrada:
        print("Baixando o .csv")
        dados = entrada.read().decode("latin1")
        print("Download completo!")

        for cidade in csv.reader(dados.splitlines()):
            print(f"{cidade[8]}: {cidade[3]}")


if __name__ == "__main__":
    read(r"http://files.cod3r.com.br/curso-python/desafio-ibge.csv")
