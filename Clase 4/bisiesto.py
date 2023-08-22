#bisiesto: int -> bool
#True si año x es bisiesto (False si no)
#ej: bisiesto(2019) -> False (no es divisible por 4)
#ej: bisiesto(2020) -> True  (divisible por 4)
#ej: bisiesto(1900) -> False (divisible por 100)
#ej: bisiesto(2000) -> True  (divisible por 400)

def bisiesto(año):
    if año%4 != 0  : 
        return False
    if año%400 == 0: 
        return True
    if año%100 == 0: 
        return False
    return True

assert not bisiesto(2019)
assert bisiesto(2020)
assert not bisiesto(1900)
assert bisiesto(2000)

#bisiesto: int -> bool
def bisiesto(año):
    return (año%4==0 and año%100!=0) or (año%400==0)
assert not bisiesto(2019)
assert bisiesto(2020)
assert not bisiesto(1900)
assert bisiesto(2000)
