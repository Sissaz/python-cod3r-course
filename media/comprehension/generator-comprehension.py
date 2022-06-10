# Generator Comprehension []

# python generator-comprehension.py
# clear

# Utiliza menos memória, pois gera dado apenas sob demanda

generator = ( i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

generator = ( i ** 2 for i in range(10) if i % 2 == 0)

for numero in generator:
    print(numero)