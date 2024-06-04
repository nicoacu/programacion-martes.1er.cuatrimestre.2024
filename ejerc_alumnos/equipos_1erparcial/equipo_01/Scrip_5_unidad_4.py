def resolver_ecuacion():
    print("A X + B = 0")
    a = float(input("Escriba el valor del coeficiente a: "))
    b = float(input("Escriba el valor del coeficiente b: "))

    if a == 0:
        if b == 0:
            print("Todos los números son solución.")
        else:
            print("La ecuación no tiene solución.")
    else:
        x = -b / a
        print(f"La ecuación tiene una solución: {x}")
#Si 'a' es igual a 0 y 'b' es diferente de 0, la ecuación no tiene solución.
#Si 'a' y 'b' son ambos iguales a 0, todos los números son solución.
#Si 'a' es diferente de 0, la ecuación tiene una solución, calculada como -b/a.
resolver_ecuacion()


# buen trabajo!

