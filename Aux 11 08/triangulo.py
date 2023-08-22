### Auxiliar 1 ###

# P3 - A.

# Simplemente seguimos las instrucciones de los enunciados. Recordemos hacer
# las recetas de diseño.
# En este caso no nos fijaremos en que sean triángulos válidos.

# perimetro: int int int -> int
# Recibe tres lados de un triángulo y retorna el perímetro.
# Ej: perimetro(2, 2, 3) retorna 7
def perimetro(a, b, c):
    return a + b + c
# Tests
assert perimetro(1, 1, 1) == 3
assert perimetro(2, 2, 3) == 7

# area: int int int -> float
# Recibe tres lados de un triángulo y retorna el área.
def area(a, b, c):
    semi = perimetro(a, b, c) / 2
    s_a = semi - a
    s_b = semi - b
    s_c = semi - c
    return (semi * s_a * s_b * s_c) ** 0.5
# Tests. Aquí hice trampa porque probé las funciones primero para ver cuánto
# daban porque no cacho áreas normales, ¡pero nunca hagan eso! La idea de
# los tests es comprobar que la función les da lo que buscan, por lo que
# el resultado lo debiesen escribir ustedes mismos antes de probar.
assert area(3, 4, 5) == 6.0
assert area(5, 5, 8) == 12.0
