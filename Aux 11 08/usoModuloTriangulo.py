### Auxiliar 1 ###

# P3 - B.

# Importamos el módulo triángulo de la otra forma.
from triangulo import *

# Haremos el programa de la misma forma que los anteriores.

print("Ingrese los tres lados del triángulo:")
a = input("Lado a: ")
b = input("Lado b: ")
c = input("Lado c: ")

# Convertimos los valores a enteros
a = int(a)
b = int(b)
c = int(c)

# Para imprimir un string junto a un valor se pueden hacer dos cosas.
# Una es simplemente ingresarlos como parámetros separados, y otra es
# transformar el valor a string para concatenarlos en un solo parámetro.
# Haremos ambas.

# Nótese que por la forma en que importamos, ya no hay que anteponer el
# nombre del archivo a las funciones.
print("Perímetro:", perimetro(a, b, c))
print("Área: " + str(area(a, b, c)))
