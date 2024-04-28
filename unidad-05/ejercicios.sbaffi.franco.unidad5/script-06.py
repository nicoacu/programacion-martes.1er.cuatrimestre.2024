# Crea un programa que permita al usuario calcular el área y el perímetro de varias figuras geométricas. El programa debe presentar un menú con las siguientes opciones:

# Calcular el área y el perímetro de un círculo.
# Calcular el área y el perímetro de un cuadrado.
# Calcular el área y el perímetro de un triángulo.
# Salir del programa.





# Área y Perímetro de un Círculo:
    # Área del círculo: Área = π × radio²
    # Perímetro del círculo: Perímetro = 2 × π × radio
# Área y Perímetro de un Cuadrado:
    # Área del cuadrado: Área = lado²
    # Perímetro del cuadrado: Perímetro = 4 × lado
# Área y Perímetro de un Triángulo:
    # Área del triángulo: Área = 0.5 × base × altura
    # Perímetro del triángulo: Suma de los 3 lados


import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2
    
    def calcular_perimetro(self):
        return 4 * self.lado

class Triangulo:
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_area(self):
        return 0.5 * self.base * self.altura
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

def mostrar_menu():
    print("1. Calcular el área y el perímetro de un círculo.")
    print("2. Calcular el área y el perímetro de un cuadrado.")
    print("3. Calcular el área y el perímetro de un triángulo.")
    print("4. Salir del programa.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            radio = float(input("Ingresá el radio del círculo: "))
            circulo = Circulo(radio)
            print("Área del círculo:", circulo.calcular_area())
            print("Perímetro del círculo:", circulo.calcular_perimetro())
        elif opcion == "2":
            lado = float(input("Ingresá el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            print("Área del cuadrado:", cuadrado.calcular_area())
            print("Perímetro del cuadrado:", cuadrado.calcular_perimetro())
        elif opcion == "3":
            base = float(input("Ingresá la base del triángulo: "))
            altura = float(input("Ingresá la altura del triángulo: "))
            lado1 = float(input("Ingresá el primer lado del triángulo: "))
            lado2 = float(input("Ingresá el segundo lado del triángulo: "))
            lado3 = float(input("Ingresá el tercer lado del triángulo: "))
            triangulo = Triangulo(base, altura, lado1, lado2, lado3)
            print("Área del triángulo:", triangulo.calcular_area())
            print("Perímetro del triángulo:", triangulo.calcular_perimetro())
        elif opcion == "4":
            print("Hasta luego!")
            break
        else:
            print("Opción no válida. Elegí una opción válida.")

if __name__ == "__main__":
    main()
