# Manipulação de Arquivos CSV

# cd 'C:\Users\sicilia.giacomazza\Documents\Python Cod3r\'
# python io_v3.py
# clear

with open ("pessoas.csv", encoding="utf-8-sig") as arquivo:

    # Criando um arquivo .txt chamado pessoas na pasta do arquivo com os dados de pessoa.csv:
    with open ("pessoas.txt", "w") as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(",")
            
            # Printando pessoas.csv no arquivo.txt
            print("Nome: {}, Idade: {}".format(*pessoa), file = saida)

            # Printando pessoas.csv no io_v3.py
            print("Nome: {}, Idade: {}".format(*pessoa))

if arquivo.closed:
    print("O arquivo já foi fechado!")

if saida.close:
    print("O arquivo de saida já foi fechado!")