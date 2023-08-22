from math import *
print("resolver ax^2 + bx + c = 0")
a=float(input("a?"))
b=float(input("b?"))
c=float(input("c?"))
if a==0:
    if b==0:
        print("ecuacion incorrecta")
    else:
        print("x=",-c/b)
else:
    d=b**2-4*a*c #discriminante
    if d==0:
        print("x=",-b/(2*a))
    elif d>0:
        r=sqrt(d)  #raiz de discrimimante
        print("x=",(-b+r)/(2*a),(-b-r)/(2*a))
    else:
        print("dos raices complejas")