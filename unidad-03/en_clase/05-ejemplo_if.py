



# Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si
# la división es exacta o no.


numero_uno = int(input("Ingrese el primer numero: "))

numero_dos = int(input("Ingrese el segundo numero: "))

resultado = numero_uno % numero_dos

if resultado == 0:
    print("El resultado es exacto")
else:
    print("El resultado no es exacto, el resto es", resultado)



