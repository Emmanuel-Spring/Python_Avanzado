"""LISTAS
Ejercicio 7. Crea un programa que pida al usuario 10 números enteros, los guarde en un array y
luego le pregunte de forma repetitiva qué número quiere buscar. Le responderá si dicho número
estaba o no entre los datos que se habían introducido inicialmente. Dejará de repetirse cuando se
introduzca el número 0."""


print("Hola, ingresa 10 números, que serán almacenados para su posterior consulta !!")
print("Ingresa el N°1 de 10 números posibles:   ")
n1 = int(input())
print("Ingresa el N°2 de 10 números posibles:   ")
n2 = int(input())
print("Ingresa el N°3 de 10 números posibles:   ")
n3 = int(input())
print("Ingresa el N°4 de 10 números posibles:   ")
n4 = int(input())
print("Ingresa el N°5 de 10 números posibles:   ")
n5 = int(input())
print("Ingresa el N°6 de 10 números posibles:   ")
n6 = int(input())
print("Ingresa el N°7 de 10 números posibles:   ")
n7 = int(input())
print("Ingresa el N°8 de 10 números posibles:   ")
n8 = int(input())
print("Ingresa el N°9 de 10 números posibles:   ")
n9 = int(input())
print("Ingresa el N°10 y final:   ")
n10 = int(input())

nums= [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
print("Que número quieres buscar:   ")

x = int(input())

if x in nums:
    print("El numero esta en esta lista")
else:
    print("El numero NO esta en esta lista")