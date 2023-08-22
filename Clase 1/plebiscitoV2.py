v1 = int(input("votos de opción 1?"))
v2 = int(input("votos de opción 2?"))
p = v1/(v1+v2)*100
pr = round(p,2)
print("porcentaje de opción 1:",pr)
print("porcentaje de opción 2:",100-pr)
