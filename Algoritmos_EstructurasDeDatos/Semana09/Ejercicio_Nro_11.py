"""FUNCIONES
Ejercicio 11. Crea una función "mostrarParesEntre", que escriba en pantalla los números pares que
hay entre los dos números que se le indiquen como parámetro (por ejemplo, 2 y 20, o 13 y 17)."""

def mostrarParesEntre(n = 100):
    pares = []

    contador = 0
    numeros = 0

    while contador < n:
        if numeros % 2 == 0:
            pares.append(numeros)
            contador += 1
        numeros += 1
    return pares

n = int(input("Esciba la cantidad de los n pares positivos: "))

if n > 0:
    pares = mostrarParesEntre(n)
    print(pares)
    print("cantidad de pares: ", len(pares))
else:
    print("El número debe ser posistivo")


# n=2
# for x in range(1,15):
#     print(n)
#     n=n*(x+1)