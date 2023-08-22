"aux"
#porcenaje(x,y): num->float
#objetivo: calcular el porcentaje de x respecto a y
#ejemplo: porcentaje(5,10) debe dar 50

def porcentaje(x,y):
    return (x/y)*100
assert porcentaje(10,50)==20