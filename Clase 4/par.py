#par: int -> bool
#True si x es par (False si es impar)	
 #ej: par(4)->True, par(5)->False
def par(x):
    if x%2==0:
        return True
    else:
        return False
assert par(4)==True   
assert par(5)==False

def par(x):
    return x%2==0 #devuelve True o False
assert par(4)   
assert not par(5)
