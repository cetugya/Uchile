"tarea 1"
def bisiesto(y):
    assert type(y) == int
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

assert bisiesto(1900)
assert not bisiesto(2021)
assert bisiesto(1600)
assert not bisiesto(1511)

def diasMes(x, y):
    assert type(x) == int and type(y) == int
    if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
        return 31
    elif x == 2:
        if bisiesto(y):
            return 29
        else:
            return 28
    else:
        return 30
assert diasMes(2, 2020) == 29
assert diasMes(8, 2023) == 31
assert not diasMes(7, 2023) == 30
assert not diasMes(2, 1511) == 29

def esFecha(z):
    assert type(z)==int
    AAAA = z // 10000
    DD = z % 100
    MD = z % 10000
    MM = MD // 100
    if 1<=AAAA and 1<=DD<=31 and 1<=MM<=12:
        return True
    else:
        return False
assert esFecha(20230822)
assert not esFecha(20230230)
assert not esFecha(20200228)
