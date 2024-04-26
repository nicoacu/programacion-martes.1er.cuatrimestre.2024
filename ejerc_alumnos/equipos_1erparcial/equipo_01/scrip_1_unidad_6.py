import random

def adivinar_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("¡Bienvenido al Juego de Adivinar el Número Secreto!")
    print("Tienes que adivinar un número entre 1 y 100.")

    while True:
        intento = int(input("Introduce tu intento: "))
        intentos += 1

        if intento < 0 or intento > 100:
            print("El número que debes ingresar debe estar entre 0 y 100.")
        elif intento < numero_secreto:
            print("Muy bajo, intenta con un número más grande.")
        elif intento > numero_secreto:
            print("Muy alto, intenta con un número más pequeño.")
        else:
            print(f"¡Felicidades! ¡Has adivinado el número secreto ({numero_secreto}) en {intentos} intentos!")
            break

adivinar_numero()



# Buen trabajo!
# Fijense la siguiente forma de escribir con print que usaron:

# print(f"¡Felicidades! ¡Has adivinado el número secreto ({numero_secreto}) en {intentos} intentos!")

#no la habíamos visto, pero se utiliza mucho en python, es una forma de concatenar strings y variables de una forma más sencilla y legible.