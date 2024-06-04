
# Lista de Tareas Pendientes:
# Crea un programa que permita al usuario mantener una lista de tareas pendientes. El programa debe permitir agregar tareas nuevas, marcar tareas como completadas y mostrar la lista actualizada de tareas.

class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

def agregar_tarea(tareas):
    descripcion = input("Ingrese la descripción de la nueva tarea: ")
    tarea_nueva = Tarea(descripcion)
    tareas.append(tarea_nueva)
    print("Tarea agregada exitosamente.")

def marcar_completada(tareas):
    mostrar_tareas(tareas)
    indice = int(input("Ingrese el número de la tarea completada: ")) - 1
    if 0 <= indice < len(tareas):
        tareas[indice].completada = True
        print("Tarea marcada como completada.")
    else:
        print("Número de tarea no válido.")

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Lista de Tareas Pendientes:")
        for i, tarea in enumerate(tareas, start=1):
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"{i}. {tarea.descripcion} - {estado}")

def main():
    tareas = []
    while True:
        print("\n--- Lista de Tareas Pendientes ---")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar tareas pendientes")
        print("4. Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            marcar_completada(tareas)
        elif opcion == "3":
            mostrar_tareas(tareas)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()


"""
En este codigo se empieza definiendo una clase llamada Tarea, la cual tiene dos atributos: descripcion y completada. El atributo completada es opcional y por defecto es False. Luego se definen tres funciones: agregar_tarea, marcar_completada y mostrar_tareas. La función agregar_tarea recibe una lista de tareas y solicita al usuario que ingrese la descripción de una nueva tarea, la crea y la agrega a la lista de tareas. La función marcar_completada recibe una lista de tareas, muestra las tareas pendientes y solicita al usuario que ingrese el número de la tarea completada. Si el número es válido, marca la tarea como completada. La función mostrar_tareas recibe una lista de tareas y muestra la lista de tareas pendientes, indicando si cada tarea está completada o pendiente. Finalmente, la función main inicializa una lista de tareas vacía y entra en un bucle que muestra un menú con cuatro opciones: agregar tarea, marcar tarea como completada, mostrar tareas pendientes y salir del programa. Dependiendo de la opción seleccionada por el usuario, se llama a la función correspondiente. El programa se ejecuta hasta que el usuario elige la opción de salir del programa.
"""