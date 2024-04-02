



# Vamos a usar while


# while condicion:
#     intrucciones 1
#     intrucciones 2
#     intrucciones 3
#     ...

contador = 0

while contador <= 5: # si está condicion es true entra al bloque
                    # si es false no entra al bloque, va a ir al else
    print("Hola Mundo!")
    print("El contador es igual a", contador)
    print("-" * 80)
    contador += 1
    # contador = contador + 1
else:
    print("El contador es igual a 6")

print("Fin del programa")

