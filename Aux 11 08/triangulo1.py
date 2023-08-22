"perimetro y area de un triangulo"

def perimetro_t(a, b ,c):
    return a + b + c
assert perimetro_t(1,1,1) == 3.0
assert perimetro_t(2,2,3) == 7.0

def area_t(a, b, c):
    semi = perimetro_t(a, b ,c) / 2
    s_a = semi - a
    s_b = semi - b
    s_c = semi - c
    return (semi * s_a * s_b * s_c) ** 0.5
assert area_t(3,4,5) == 6.0
assert area_t(5,5,8) == 12.0