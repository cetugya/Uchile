#modulo circulo: en archivo circulo.py
#datos y funciones para circulos

PI=3.14

#perimetro: num -> float
#perimetro de circulo de radio r
#ejemplo: perimetro(1) -> 6.28
def perimetro(r):
    return 2*PI*r
assert perimetro(1)==6.28

#area: num -> float
#area de circulo de radio r
#ejemplo: area(1) -> 3.14
def area(r):
    return PI*r**2
assert area(1)==3.14
