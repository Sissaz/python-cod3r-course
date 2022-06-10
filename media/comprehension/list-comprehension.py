# List Comprehension []

# [Expression for item in list if condicional]

# python list-comprehension.py
# clear

# Versão Alternativa

dobro = [i * 2 for i in range (10)]
print(dobro)

dobro_pares = [ i * 2 for i in range(10) if i % 2 == 0]
print(dobro_pares)


# Versão Normal

mult = []
for i in range(10):
    mult.append(i * 2)
print(mult)

mult_pares = []
for i in range(10):
    if i % 2 == 0:
        mult_pares.append(i * 2)
print(mult_pares)







