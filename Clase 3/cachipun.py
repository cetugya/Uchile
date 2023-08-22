"piedra, papel o tijeras"
from random import *
n=randint(1,3)
if n==1:
    JUGADA ="piedra"
elif n==2:
    JUGADA ="papel"
else:
    JUGADA ="tijeras"
print(JUGADA)