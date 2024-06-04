# Inicializamos la lista de productos
productos = []

# Función para agregar un nuevo producto
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad disponible: "))
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    productos.append(producto)
    print("Producto agregado con éxito.")

# Función para actualizar la cantidad disponible de un producto
def actualizar_cantidad():
    nombre = input("Ingrese el nombre del producto que desea actualizar: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            nueva_cantidad = int(input("Ingrese la nueva cantidad disponible: "))
            producto["cantidad"] = nueva_cantidad
            print("Cantidad actualizada con éxito.")
            return
    print("Producto no encontrado.")

# Función para mostrar la lista de productos en stock
def mostrar_inventario():
    print("Inventario actual:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad disponible: {producto['cantidad']}")

# Menú principal
def menu():
    while True:
        print("\n1. Agregar producto")
        print("2. Actualizar cantidad de un producto")
        print("3. Mostrar inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            actualizar_cantidad()
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()



# Buen trabajo! El código funciona correctamente y cumple con los requerimientos del ejercicio.
# Pero hay muchas cosas que no vimos, este tipo de ejercicios no los voy a tomar en el primer parcial....
# Hay tipos de datos que son tipo lista y tipos de datos que sin diccionario, ya vamos a ver en las siguientes clases.

