# Contador de Caracteres Específicos:

# Crea un programa que solicite al usuario ingresar una letra o carácter. El programa debe contar y mostrar cuántas veces aparece ese carácter en una frase dada. El procedimiento es el siguiente:
# Pide al usuario que ingrese una frase.
# Luego, pide al usuario que ingrese un carácter para buscar en la frase.
# Utiliza un bucle for junto con índices para recorrer la frase y contar las ocurrencias del carácter especificado.
# Muestra el número total de veces que aparece ese carácter en la frase.


# Acá se le solicita al usuario que ingrese una frase
frase = input("Ingresa una frase: ")

# Se le solcita al usuario que ingrese un carácter para buscar en la frase
caracter = input("Ingresa un carácter para buscar en la frase: ")

# Utilizo "count" para contar las ocurrencias del carácter especificado
ocurrencias = frase.count(caracter)

# Mostrar el número total de veces que aparece el carácter en la frase
print(f"El carácter '{caracter}' aparece {ocurrencias} veces en la frase.")
