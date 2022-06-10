# Manipulação de Arquivos CSV

# cd 'C:\Users\sicilia.giacomazza\Documents\Python Cod3r\'
# python io_v2.py
# clear

with open ("pessoas.csv", encoding="utf-8-sig") as arquivo:
    for registro in arquivo:
        print("Nome: {}, Idade: {}".format(*registro.strip().split(",")))

if arquivo.closed:
    print("O arquivo foi fechado!")

