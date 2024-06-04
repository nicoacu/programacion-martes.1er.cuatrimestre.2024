# Juego de Adivinar el Número Secreto:
# Desarrolla un programa en el que la computadora elija un número aleatorio entre 1 y 100. El usuario deberá intentar 
# adivinar ese número. El programa debe proporcionar pistas, después de cada intento del usuario hasta que adivine correctamente.
# Con respecto a las pistas, si bien está abierto a como quieras resolverlo la idea es ir avisando si está muy alejado, 
# mas o menos alejado, cerca, muy cerca, etc. Pudiendo avisar si el número es mayor o menor al que se intenta adivinar.

import random

def obtener_pista(num_secreto, intento):
    if intento < num_secreto - 20:
        return 'Estas muy lejos'
    elif intento < num_secreto - 10:
        return 'No estas tan lejos'
    elif intento < num_secreto - 5:
        return 'Estas muy cerca'
    elif intento < num_secreto:
        return 'Estás muy cerca'
    elif intento > num_secreto + 20:
        return 'Estás muy lejos'
    elif intento > num_secreto + 10:
        return 'Estás bastante lejos'
    elif intento > num_secreto + 5:
        return 'Estás algo lejos'
    elif intento > num_secreto:
        return 'Estás muy cerca'
    else:
        return f'Adivinaste!, el numero secreto era {intento}'

def juego_adivinar_numero():
    num_secreto = random.randint(1, 100)
    intentos = 0 

    print('Juego de Adivinar el Número Secreto')
    print('Debe adivinar un numero entre 1 y 100')

    while True:
        dato = input('Ingrese el numero o ingrese salir para finalizar el programa:  ')

        if dato.lower() == 'salir':
            print('El numero secreto era', num_secreto)
            break

        if not dato.isdigit():
            print('Ingresar solo numeros, o "salir" si quiere finalizar el programa')
            continue

        intento = int(dato)
        intentos += 1

        if intento < 1 or intento > 100:
            print('El numero tiene que estar entre 1 y 100')
            continue

        if intento >= 1 and intento <= 100:
            pista = obtener_pista(num_secreto, intento)
            print(pista)

        if intento == num_secreto:
            break

juego_adivinar_numero()



# Buen trabajo!
#        return f'Adivinaste!, el numero secreto era {intento}'

# Esa forma de escribir print la vamos a ver en clase, se utiliza mucho