import csv

with open("pessoas.csv", encoding="utf-8-sig") as entrada:
    for pessoa in csv.reader(entrada):
        print("Nome: {}, Idade: {}".format(*pessoa))