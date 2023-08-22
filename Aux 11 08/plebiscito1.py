"plebiscito"

print("votos por el apruebo?")
v1 = int(input())

print("votos por el rechazo?")
v2 = int(input())

print("votos en blanco?")
v3 = int(input())

print("votos nulos?")
v4 = int(input())

vt = v1 + v2 + v3 + v4
print("votos totales?", vt)

pa = round((v1 / vt)*100, 2)

pr = round((v2 / vt)*100, 2)

pb = round((v3 / vt)*100, 2)

pn = round((v4 / vt)*100, 2)

print("porcentaje apruebo", pa)

print("porcentaje rechazo", pr)

print("porcentaje blancos", pb)

print("porcentaje nulos", pn)
