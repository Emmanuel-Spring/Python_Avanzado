"""TUPLAS
Ejercicio 1. El tiempo como tuplas. Proponer una representación con tuplas para representar el
tiempo. Escribir una función sumaTiempo que reciba dos tiempos dados y devuelva su suma.
"""

""" Template: Trabajo de Python
Semana Nro 9
Integrantes: Emmauel Nieto Muñoz
             Felipe Belmar Belmar
Fecha: Jueves 03 de Junio del 2021"""

from datetime import date

hoy = date(2021, 6, 6)
otro_dia = date(2025, 11, 21)

dias_diferencia = hoy - otro_dia

print("*****************************************************")
print("*****************************************************")
print(f"Los días de diferencia entre {hoy} y {otro_dia} es:")
print(f"{abs(dias_diferencia.days)} días")
print("*****************************************************")
print("*****************************************************")