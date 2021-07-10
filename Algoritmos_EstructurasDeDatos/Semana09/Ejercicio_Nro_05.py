"""CONJUNTOS
Ejercicio 5. Llenar un conjunto con 10 números aleatorios entre 0 y 100"""

from random import randint

def genrar_numeros_aleatorios(n=10):
    numeros_10 = []

    while True:
        numeros = [randint(1, 101) for _ in range(n)]

        if all(x >= 0 and x <= 100 for x in numeros):
            numeros_10 = numeros
            break

    return numeros_10

print("******************************************")
print("******************************************")
print("Los 10 números aleatorios entre 0 y 100 son:")
print(genrar_numeros_aleatorios(10))
print("******************************************")
print("******************************************")
