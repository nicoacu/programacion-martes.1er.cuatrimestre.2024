# Juego de Adivinar el Número Secreto:
# Desarrolla un programa en el que la computadora elija un número aleatorio entre 1 y 100. El usuario deberá intentar adivinar ese número. El programa debe proporcionar pistas, después de cada intento del usuario hasta que adivine correctamente.
# Con respecto a las pistas, si bien está abierto a como quieras resolverlo la idea es ir avisando si está muy alejado, mas o menos alejado, cerca, muy cerca, etc. Pudiendo avisar si el número es mayor o menor al que se intenta adivinar.

import random

# Generar un número aleatorio entre 1 y 100 como el número secreto
numero_secreto = random.randint(1, 100)

# Mensaje de bienvenida
print("Bienvenido al Juego de Adivinar el Número Secreto!")
print("Intenta adivinar el número secreto, que está entre 1 y 100.")

# Bucle para permitir múltiples intentos del usuario
while True:
    # Pedir al usuario que ingrese un número
    intento = int(input("Ingresa un número: "))
    
    # Comparar el número ingresado con el número secreto
    if intento == numero_secreto:
        print("¡Felicidades! ¡Adivinaste el número secreto!")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
    
    # Dar pistas adicionales basadas en la diferencia entre el número secreto y el intento del usuario
    diferencia = abs(numero_secreto - intento)
    if diferencia > 50:
        print("Estás muy lejos.")
    elif diferencia > 20:
        print("Estás bastante alejado.")
    elif diferencia > 10:
        print("Estás cerca.")
    else:
        print("Estás muy cerca.")



