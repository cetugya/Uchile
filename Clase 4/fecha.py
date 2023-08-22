"tarea 1"
def bisiesto(year):
    assert type(year) == int
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

assert not bisiesto(1900)
assert not bisiesto(2021)
assert bisiesto(1600)
assert not bisiesto(1511)

def diasMes(mes, year):
    assert type(mes) == int and type(year) == int
    if 1<=mes<=12 and 1<=year:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            return 31
        elif mes == 2:
            if bisiesto(year):
                return 29
            else:
                return 28
        else:
            return 30
    else:
        return 'Fecha Invalida'
assert diasMes(2, 2020) == 29
assert diasMes(8, 2023) == 31
assert not diasMes(7, 2023) == 30
assert not diasMes(2, 1511) == 29

def esFecha(fecha):
    assert type(fecha) == int
    AAAA = fecha // 10000
    MD = fecha % 10000
    MM = MD // 100
    DD = MD % 100
    if 1<=AAAA and 1<=MM<=12:
        if MM == 2:
            if bisiesto(AAAA):
                return 1<=DD<=29
            else:
                return 1<=DD<=28
        elif MM == 1 or MM == 3 or MM == 5 or MM == 7 or MM == 8 or MM == 10 or MM == 12:
            return 1<=DD<=31
    else:
        return 1<=DD<=30
    return False
assert esFecha(20230822)
assert not esFecha(20232232)
assert esFecha(20200228)

def diferencia(fecha1 , fecha2):
    assert type(fecha1)==int and type(fecha2)==int
    year1 = fecha1 // 10000
    month1 = (fecha1 % 10000) // 100
    day1 = fecha1 % 100
    year2 = fecha2 // 10000
    month2 = (fecha2 % 10000) // 100
    day2 = fecha2 % 100
    diff = abs(year1 - year2)
    if  1<=year1 and 1<=month1<=12 and 1<=year2 and 1<=month2<=12:
        if fecha1>fecha2:
            if month1 > month2 or (month1 == month2 and day1 > day2):
                return diff
            else:
                return diff-1
        elif fecha2>fecha1:
            if month2 > month1 or (month2 == month1 and day2 > day1):
                return diff
            else:
                return diff-1
        elif fecha1==fecha2:
            return 0



def escribir(date):
    YY = date // 10000
    M = (date % 10000) // 100
    D = (date % 10000) % 100
    if 1<=M<=12 and 1<=D<=31 and 1<=YY:
        if M == 1:
            mes = "Enero"
        elif M == 3:
            mes = "Marzo"
        elif M == 4:
            mes = "Abril"
        elif M == 5:
            mes = "Mayo"
        elif M == 6:
            mes = "Junio"
        elif M == 7:
            mes = "Julio"
        elif M == 8:
            mes = "Agosto"
        elif M == 9:
            mes = "Septiembre"
        elif M == 10:
            mes = "Octubre"
        elif M == 11:
            mes = "Noviembre"
        elif M == 12:
            mes = "Diciembre"
        elif M == 2:
            if bisiesto(YY) and 1<=D<=29:
                mes = "Febrero"
            elif not bisiesto(YY) and 1<=D<=28:
                mes = "Febrero"
            else:
                return "Fecha Invalida"
        return str(D) + " " +mes+ " " + str(YY)
    else:
        return "Fecha invalida"
