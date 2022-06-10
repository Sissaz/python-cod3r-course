# Manipulação de Arquivos CSV

# cd 'C:\Users\sicilia.giacomazza\Documents\Python Cod3r\'
# python io_v1.py
# clear

try:
    arquivo = open("pessoas.csv", encoding="utf-8-sig")
    for registro in arquivo:
        print("Nome: {}, Idade: {}".format(*registro.strip().split(",")))

except IndexError:
    pass

finally:
    print("Finalizado")
    arquivo.close()

if arquivo.closed:
    print("O arquivo foi fechado!")

