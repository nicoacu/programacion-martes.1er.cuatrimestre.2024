
# Gestor de Inventario de Tienda:
# Crea un sistema simple de gestión de inventario para una tienda. El programa debe permitir agregar productos nuevos, actualizar la cantidad disponible de un producto y mostrar la lista actualizada de productos en stock.

class Inventario:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, nombre_producto, cantidad):
        if nombre_producto in self.inventario:
            self.inventario[nombre_producto] += cantidad
        else:
            self.inventario[nombre_producto] = cantidad

    def actualizar_cantidad(self, nombre_producto, cantidad):
        if nombre_producto in self.inventario:
            self.inventario[nombre_producto] = cantidad
        else:
            print("El producto no está en el inventario.")

    def mostrar_inventario(self):
        print("\nInventario de la Tienda:")
        if self.inventario:
            for producto, cantidad in self.inventario.items():
                print(f"{producto}: {cantidad}")
        else:
            print("El inventario está vacío.")

def main():
    inventario_tienda = Inventario()
    while True:
        print("\n--- Gestor de Inventario de Tienda ---")
        print("1. Agregar Producto")
        print("2. Actualizar Cantidad de Producto")
        print("3. Mostrar Inventario")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            inventario_tienda.agregar_producto(nombre_producto, cantidad)
        elif opcion == "2":
            nombre_producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            inventario_tienda.actualizar_cantidad(nombre_producto, cantidad)
        elif opcion == "3":
            inventario_tienda.mostrar_inventario()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
