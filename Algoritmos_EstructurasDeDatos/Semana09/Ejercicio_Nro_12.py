"""FUNCIONES
Ejercicio 12. 2. Escribir una función que permita imprimir los "N" primeros números de la
siguiente serie:
2 4 12 48 240 1440"""
# 2x1=2 2x2=4 4x3=12 12x4=48 48x5=240 240x6=1440

x= int(input("Ingrese n"))

def NprimerosNumeros(n=2):

    for x in range(1,15):
        n = 0
        n=n*(x+1)


print(NprimerosNumeros)

