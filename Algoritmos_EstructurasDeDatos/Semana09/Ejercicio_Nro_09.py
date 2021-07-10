"""CADENAS
Ejercicio 9. Crea un programa que pida su nombre al usuario y diga cuántas vocales contiene"""

nombre = input("Ingresa tu nombre: ")

def vocales(nombre):
	conteo = 0
	for letra in nombre:
		if letra in "aeiou":
			conteo += 1
	return conteo
cantidad = vocales(nombre)

print("**************************************************")
print("**************************************************")
print(f"El nombre ingresado es: {nombre} y tiene {cantidad} vocales.")
print("**************************************************")
print("**************************************************")
