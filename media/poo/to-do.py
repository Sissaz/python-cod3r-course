from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + ("(Concluída)" if self.feito else'')


def main():
    casa = []
    casa.append(Tarefa("Passar a roupa"))
    casa.append(Tarefa("Lavar os pratos"))

    [tarefa.concluir() for tarefa in casa if tarefa.descricao == "Lavar os pratos"]
    for tarefa in casa:
        print(f'-{tarefa}')


if __name__ == "__main__":
    main()
