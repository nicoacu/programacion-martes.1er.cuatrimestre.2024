

alumno_nombre = "Patricio"
alumno_edad = 17

print( alumno_nombre + " tiene " + str(alumno_edad) + " años" )
print("-" * 80)

match alumno_edad:
    case 18:
        print(alumno_nombre + " tiene 18 años")
        print("El alumno " + alumno_nombre + " es mayor de edad")
        print("Puede ingresar al bar")
    case 17:
        print(alumno_nombre + " tiene 17 años")
        print("El alumno " + alumno_nombre + " es menor de edad, tiene 17 años")
        print("Puede ingresar al bar con un mayor de edad")
        print("Puede ingresar al bar con un mayor de edad")
    case 16:
        print(alumno_nombre + " tiene 16 años")


# Ahora vamos a utilizar match con condiciones
print("-" * 80)
print("Ahora vamos a utilizar match con condiciones")
print("-" * 80)
alumno_nombre = "Patricio"
alumno_edad = 10

print( alumno_nombre + " tiene " + str(alumno_edad) + " años" )
print("-" * 80)

match alumno_edad:
    case _ if alumno_edad >= 18:
        print(alumno_nombre + " tiene " + str(alumno_edad) + " años")
        print("El alumno " + alumno_nombre + " es mayor de edad")
        print("Puede ingresar al bar")
    case _ if alumno_edad >= 12:
        print(alumno_nombre + " tiene " + str(alumno_edad) + " años")
        print("El alumno " + alumno_nombre + " es menor de edad")
        print("Puede ingresar al bar con un mayor de edad")
    case _:
        print(alumno_nombre + " tiene " + str(alumno_edad) + " años")
        print("El alumno " + alumno_nombre + " es menor de  12 años")
        print("No puede ingresar al bar")


