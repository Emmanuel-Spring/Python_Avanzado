"""Vídeo N° 24 Determina si eres mayor de edad"""

edadAdulto = 18
edadPersona = int(input("Ingresa tu edad: "))

if edadPersona >= edadAdulto:
    print(f"La persona con edad {edadPersona} es un adulto")
else:
    print(f"La persona con edad {edadPersona} es un menor de edad")