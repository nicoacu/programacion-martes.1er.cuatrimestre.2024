# Detector de Palíndromos:

# Desarrolla un programa que verifique si una palabra ingresada por el usuario es un palíndromo (una palabra que se lee igual de adelante hacia atrás). El proceso es el siguiente:
# Pide al usuario que ingrese una palabra.
# Utiliza un bucle for junto con índices para recorrer la mitad del string y comparar los caracteres desde el principio con los caracteres desde el final.
# Si todos los caracteres coinciden, indica que la palabra es un palíndromo; de lo contrario, indica lo contrario.

# Solicitar al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")

# Convertir la palabra a minúsculas
palabra = palabra.lower()

# Inicializar una bandera para indicar si la palabra es un palíndromo
es_palindromo = True

# Utilizar un bucle for junto con índices para recorrer la mitad del string
for i in range(len(palabra) // 2):
    # Comparar los caracteres desde el principio con los caracteres desde el final
    if palabra[i] != palabra[-(i + 1)]:
        # Si hay al menos una diferencia, la palabra no es un palíndromo
        es_palindromo = False
        # Salir del bucle porque ya no es necesario seguir verificando
        break

# Verificar si la palabra es un palíndromo
if es_palindromo:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
