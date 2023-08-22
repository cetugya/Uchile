from porcentaje import *

print("cabtidad de votos por opcion")

v1 = int(input("votos del apruebo?") )

v2 = int(input("votos del rechazo?") )

v3 = int(input("votos en blanco?") )

v4 = int(input("votos nulos?") )

vt = v1 + v2 + v3 + v4

print("votos totales?", vt)

print("porcentaje apruebo?", round(porcentaje(v1,vt), 1))

print("porcentaje rechazo?", round(porcentaje(v2,vt), 1))

print("porcentaje votos blancos?", round(porcentaje(v3,vt), 1))

print("porcentaje votos nulos?", round(porcentaje(v4,vt), 1))

vr = v1 + v2

print("porcentaje de votos sin contar los blancos y nulos:")

print("apruebo?", round(porcentaje(v1,vr), 2))

print("rechazo?", round(porcentaje(v2,vr), 2))