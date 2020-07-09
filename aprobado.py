# autor DE LA CRUZ QUISPE ROYER ALVARO
#EJERCICIO QUE DETERMINE SI UN ALUMNO ESTA APROBADO O NO.

def determinarAprobado(promedio):
    if promedio >= 11:
        resultado = "Aprobado"
    else:
        resultado = "Desaprobado"
    return resultado

promedios =int(input("Promedio = "))
print(determinarAprobado(promedios))