# Función para calcular el área y el perímetro de un círculo


def calcular_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    area = 3.14 * radio ** 2
    perimetro = 2 * 3.14 * radio
    print("El área del círculo es:", area)
    print("El perímetro del círculo es:", perimetro)

# Función para calcular el área y el perímetro de un cuadrado
def calcular_cuadrado():
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    area = lado ** 2
    perimetro = 4 * lado
    print("El área del cuadrado es:", area)
    print("El perímetro del cuadrado es:", perimetro)

# Función para calcular el área y el perímetro de un triángulo
def calcular_triangulo():
    base = float(input("Ingrese la longitud de la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    lado1 = float(input("Ingrese la longitud de un lado del triángulo: "))
    lado2 = float(input("Ingrese la longitud de otro lado del triángulo: "))
    perimetro = base + lado1 + lado2
    print("El área del triángulo es:", area)
    print("El perímetro del triángulo es:", perimetro)

# Menú principal
def menu():
    while True:
        print("\n¿Qué figura geométrica desea calcular?")
        print("1. Círculo")
        print("2. Cuadrado")
        print("3. Triángulo")
        print("4. Salir del programa")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            calcular_circulo()
        elif opcion == "2":
            calcular_cuadrado()
        elif opcion == "3":
            calcular_triangulo()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()




# Buen trabajo, si utilizaron chatgpt para hacer el código, lo más importante es que lo entiendan bien y vayan adaptando según sus conocimientos.


