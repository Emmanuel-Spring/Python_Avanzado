"""CADENAS
Ejercicio 8. Crea un programa que pida su nombre al usuario y lo escriba alternando letras
mayúsculas y minúsculas (por ejemplo, "Nacho" se mostraría como "NaChO"""

print("Ingresa tu nombre:   ")
nombre = input()

resultado = ''

for i in range(0, len(nombre)):
    if (i % 2) == 0:
        resultado += nombre[i].upper()
    else:
        resultado += nombre[i].lower()

print("*********************************************")
print("*********************************************")
print(f"El nombre ingresado es {nombre} y el resultado es: ")
print(resultado)
print("*********************************************")
print("*********************************************")