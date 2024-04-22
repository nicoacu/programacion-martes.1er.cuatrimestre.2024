
# Calculadora de Propina:
# Desarrolla una calculadora de propinas que solicite al usuario ingresar el total de la cuenta en un restaurante. El programa debe calcular automáticamente diferentes opciones de propinas (por ejemplo, 15%, 18%, 20%) y mostrar el monto total a pagar incluyendo la propina.

def calcular_propina(total_cuenta, porcentaje_propina):
    try:
        total_cuenta = float(total_cuenta)
        porcentaje_propina = float(porcentaje_propina)
        if total_cuenta < 0 or porcentaje_propina < 0 or porcentaje_propina > 100:
            raise ValueError
        propina = total_cuenta * (porcentaje_propina / 100)
        total_a_pagar = total_cuenta + propina
        return propina, total_a_pagar
    except ValueError:
        print("Error: Por favor, ingrese números válidos.")
        return None, None

def mostrar_opciones_propina():
    print("Opciones de propina disponibles:")
    print("1. 15%")
    print("2. 18%")
    print("3. 20%")

def main():
    print("¡Bienvenido a la Calculadora de Propina!")
    total_cuenta = input("Ingrese el total de la cuenta en el restaurante: ")

    while True:
        mostrar_opciones_propina()
        opcion = input("Seleccione una opción de propina (1/2/3): ")

        if opcion == "1":
            propina, total_a_pagar = calcular_propina(total_cuenta, 15)
            break
        elif opcion == "2":
            propina, total_a_pagar = calcular_propina(total_cuenta, 18)
            break
        elif opcion == "3":
            propina, total_a_pagar = calcular_propina(total_cuenta, 20)
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    if propina is not None and total_a_pagar is not None:
        print(f"Propina: ${propina:.2f}")
        print(f"Total a pagar incluyendo propina: ${total_a_pagar:.2f}")

if __name__ == "__main__":
    main()
