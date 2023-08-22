def diferencia_años(fecha1, fecha2):
    assert type(fecha1) == int and type(fecha2) == int
    
    año1 = fecha1 // 10000
    mes1 = (fecha1 // 100) % 100
    dia1 = fecha1 % 100
    
    año2 = fecha2 // 10000
    mes2 = (fecha2 // 100) % 100
    dia2 = fecha2 % 100
    
    if fecha1 > fecha2:
        año1, año2 = año2, año1
        mes1, mes2 = mes2, mes1
        dia1, dia2 = dia2, dia1
    
    diferencia_años = año2 - año1
    
    if mes2 < mes1 or (mes2 == mes1 and dia2 < dia1):
        diferencia_años -= 1
    
    return diferencia_años

# Ejemplo de uso
fecha1 = 20230819
fecha2 = 20220820

diferencia = diferencia_años(fecha1, fecha2)
print(f"Diferencia de años: {diferencia}")

print("prueba", diferencia_años(20230830, 20210830))
