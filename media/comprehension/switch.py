# Simulando o Switch

# cd 'C:\Users\sicilia.giacomazza\Documents\Python Cod3r\'
# python switch.py
# clear

def get_tipo_dia(dia):
    dias = {
        (1, 7): "Fim de Semana",
        tuple(range(2, 7)): "Dia de Semana",    
    }
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(dia_escolhido, "** dia inválido **")

if __name__ == "__main__":
    for dia in range(0, 9):
        print(f"{dia}: {get_tipo_dia(dia)}")