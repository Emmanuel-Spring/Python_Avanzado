"""TUPLAS
Ejercicio 2. Escribir una función diaSiguienteE que dada una fecha expresada como la terna (Día,
Mes, Año) (donde Día, Mes y Año son números enteros) calcule el día siguiente al dado, en el
mismo formato."""

from datetime import date
from getpass import _raw_input


def fecha_dia(dia, mes, annio):
    bisiesto = False

    if annio % 400 == 0:
        bisiesto = True
    elif annio % 4 == 0:
        bisiesto = True

    if mes in (1,3,5,7,8,10,12):
        dias_mes =31
    elif mes == 2:
        if bisiesto:
            dias_mes = 29
        else:
            dias_mes = 28
    else:
        dias_mes = 30

    if dia < dias_mes:
        dia += 1
    else:
        dia = 1
        if mes == 12:
            mes = 1
            annio += 1
        else:
            mes += 1

    return (dia, mes, annio)


print("Ingrese la fecha:   ");
dia = int(_raw_input("Ingrese un día del mes (1-31): "))
mes = int(_raw_input("Ingrese un mes del año (1-12): "))
annio = int(_raw_input("Ingrese un año (1900 - 2200): "))

print(f"Los datos ingresados son los siguiente: ")
print(f"el día {dia}, el mes {mes} y el año {annio}")
print("****************************************")
print("****************************************")
print("Ahora si le agregamos un día a la fecha ingresada es: ")
print(fecha_dia(dia, mes, annio))

