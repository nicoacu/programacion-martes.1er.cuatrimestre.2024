
# Simulador de Carrera de Autos:
# Implementa un programa que simule una carrera de autos entre varios competidores. Cada competidor tiene una velocidad aleatoria y la carrera se desarrolla en rondas. El programa debe mostrar el progreso de la carrera en cada ronda y determinar el ganador al final.

import random

# Definir el número de competidores y la cantidad de rondas
num_competidores = 5
num_rondas = 10

# Lista para almacenar las posiciones de los competidores en cada ronda
posiciones = [0] * num_competidores

# Mensaje de inicio de la carrera
print("¡Comienza la carrera de autos!")

# Bucle para simular las rondas de la carrera
for ronda in range(1, num_rondas + 1):
    print(f"\nRonda {ronda}:")
    
    # Simular el avance de cada competidor en esta ronda
    for competidor in range(num_competidores):
        # Generar una velocidad aleatoria para el competidor
        velocidad = random.randint(1, 10)
        
        # Actualizar la posición del competidor según su velocidad
        posiciones[competidor] += velocidad
        
        # Mostrar el progreso del competidor en esta ronda
        print(f"Competidor {competidor + 1}: {'-' * posiciones[competidor]}")
    
    # Esperar un poco antes de la siguiente ronda para dar un efecto de animación
    input("\nPresiona Enter para continuar con la siguiente ronda...")
    print("\n" + "=" * 50)

# Determinar al ganador al final de la carrera
ganador = posiciones.index(max(posiciones)) + 1
print(f"\n¡El ganador de la carrera es el Competidor {ganador}!")
