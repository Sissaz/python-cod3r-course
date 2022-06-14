# POO

# Membros e Construtores

from tkinter import dialog

class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        """Construtor para criar a instancia dos objetos"""
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 2019
print(d1)

d2 = Data()
d2.dia = 7
d2.mes = 11
d2.ano = 2020
print(d2)
