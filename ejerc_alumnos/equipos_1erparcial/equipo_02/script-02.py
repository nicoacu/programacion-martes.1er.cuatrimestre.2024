
# Lista de Tareas Pendientes:
# Crea un programa que permita al usuario mantener una lista de tareas pendientes. El programa debe permitir agregar 
# tareas nuevas, marcar tareas como completadas y mostrar la lista actualizada de tareas.

def main():
    tareas = []

    while True:
        print('\nLista de Tareas Pendientes\n')
        print('1. Agregar tarea')
        print('2. Marcar tarea como completada')
        print('3. Mostrar tareas')
        print('4. Salir')

        opcion = int(input('Elige una opción: '))

        if opcion == 1:
            tarea = input('Ingresa la nueva tarea: ')
            print('----------------------------------')
            tareas.append({'tarea': tarea, 'completada': False})
        elif opcion == 2:
            indice = int(input('Ingresa el número de la tarea a marcar como completada: '))
            if indice.isdigit() and  0 <= indice < len(tareas):
                tareas[indice]['completada'] = True
            else:
                print('El undice no es valido')
            print('----------------------------------')
        elif opcion == 3:
            if not tareas:
                print('No hay tareas pendientes.')
                print('----------------------------------')
            for i, tarea in enumerate(tareas):
                print(f'{i}. {'[X]' if tarea['completada'] else '[ ]'} {tarea['tarea']}')
        elif opcion == 4:
            break
        else:
            print('Opción no válida. Por favor, elige una opción del menú.')
            print('----------------------------------')


main()

# este ejercicio es muy complejo, lo ubiqué mal en esta sección
# en este caso da un error, pero dejamos para resolver para más adelante

# lo siguiente es una forma también muy compleja de hacer un bucle quizá más adelante la vemos
# for i, tarea in enumerate(tareas):
#                 print(f'{i}. {'[X]' if tarea['completada'] else '[ ]'} {tarea['tarea']}')

# y el error que dá:

# equipos_1erparcial/equipo_02 $ python script-02.py 
#   File "/var/www/html/istea/infra/programacion-martes.1er.cuatrimestre.2024/ejerc_alumnos/equipos_1erparcial/equipo_02/script-02.py", line 34
#     print(f'{i}. {'[X]' if tarea['completada'] else '[ ]'} {tarea['tarea']}')
#                    ^
# SyntaxError: f-string: expecting '}'
#  equipos_1erparcial/equipo_02 $ python script-02.py 
#   File "/var/www/html/istea/infra/programacion-martes.1er.cuatrimestre.2024/ejerc_alumnos/equipos_1erparcial/equipo_02/script-02.py", line 34
#     print(f'{i}. {'[X]' if tarea['completada'] else '[ ]'} {tarea['tarea']}')
#                    ^
# SyntaxError: f-string: expecting '}'
