"""CONJUNTOS
Ejercicio 4. ¿Como puedo agregar al conjunto A?. Los números 1, 2 y 3 en una única operación."""


A = { 'z', 8 , 9 , (10,20,30) , 8 , 9 , 8}
print("Conjunto inicial: ")
print(A)

print("**************************************")
print("**************************************")
lista_actualizada = {1, 2, 3}
A.update(lista_actualizada)
print("Conjunto actualizado: ")
print(A)

# Ejecución de Consola
# {8, 9, 'z', (10, 20, 30)}
# {1, 2, 3, 8, 9, 'z', (10, 20, 30)}