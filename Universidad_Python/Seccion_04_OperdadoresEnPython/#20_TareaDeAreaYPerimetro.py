"""En el siguiente ejercicio se solicita calcular el área y el perímetro de un Rectángulo, para ello deberemos crear las siguientes variables:

alto (int)

ancho (int)

El usuario debe proporcionar los valores de largo y ancho, y después se debe imprimir el resultado en el siguiente formato(no usar acentos y respetar los espacios, mayúsculas, minúsculas y saltos de línea):

Proporciona el alto:
Proporciona el ancho:
Area: <area>
Perímetro: <perimetro>
Las fórmulas para calcular el área y el perímetro de un Rectángulo son:

Área: alto * ancho

Perímetro: (alto + ancho) * 2

Nota: Recordar que las tareas no cambian de estado y no afectan en el avance de tu curso ni en la generación de tu certificado de finalización del curso en Udemy.

Preguntas de esta tarea
¿Cuál es el código del requerimiento solicitado?"""

ladoA = 15
ladoB = 20

perimetro = 2*(ladoB + ladoA)
area = ladoB * ladoA

print("Rectángulo de lados 15 y 20 centímetros:")
print("*************************************************")
print(f"El perímetro del rectángulo es {perimetro} centímetros")

print("*************************************************")
print(f"El Área del rectángulo es {area} centímetros cuadrados")