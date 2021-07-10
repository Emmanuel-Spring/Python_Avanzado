"""LISTAS
Ejercicio 6. Crea un programa que pida al usuario 10 números enteros y luego muestre los que
eran pares, todos ellos en la misma línea separados por un espacio en blanco."""



numeroEntero = int(input("Ingrese 10 números: "))

def NPrimerosNumeros (numeroEntero):
    if numeroEntero > 0 :
        resultado = []

        for n in range (1, 11):
            if n % 2 == 0 :
             resultado.append(n)
        return resultado
    raise ValueError("Error de número")

numerosImpresos = NPrimerosNumeros (numeroEntero)


print("ingrese 10 números:  ")
print(numerosImpresos)