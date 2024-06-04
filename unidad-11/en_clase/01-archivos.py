


# Sistema Windows
# C:\Users\usuario\Documents\archivo.txt

# Sistema Unix / Linux
# /var/www/html/istea/infra/programacion-martes.1er.cuatrimestre.2024/unidad-11/en_clase/archivo_ejemplo.txt

# En los sistemas Unix / Linux, los archivos y directorios se separan con una barra inclinada (/)
# En los sistemas Windows, los archivos y directorios se separan con una barra invertida (\)

# Para Windows
# c:\archivo.txt
# c:\Users\archivo.txt
# c:\Users\ARCHIVO.txt

# Unix / Linux
# /home/usuario/archivo.txt
# /home/usuario/ARCHIVO.txt # son dos archivos distintos

# Ruta absoluta y Ruta relativa

# Ruta absoluta
# C:\Users\usuario\Documents\archivo.txt
# /var/www/html/istea/infra/programacion-martes.1er.cuatrimestre.2024/unidad-11/en_clase/archivo_ejemplo.txt

# Ruta relativa
# archivo.txt -> Si estamos dentro de la carpeta C:\Users\usuario\Documents
# unidad-11/en_clase/archivo_ejemplo.txt -> Si estamos dentro de la carpeta /var/www/html/istea/infra/programacion-martes.1er.cuatrimestre.2024

# streams


ruta_absoluta_archivo = '/var/www/html/istea/infra/programacion-martes.1er.cuatrimestre.2024/unidad-11/en_clase/archivo_ejemplo.txt'

try:
    stream = open(ruta_absoluta_archivo, "r", encoding="utf-8")
    print("El archivo se abrió correctamente")
    
    contador = 0

    caracter = stream.read(1)
    while caracter != '':
        print(caracter, end="")
        caracter = stream.read(1)
        contador += 1

    # En este bloque salio del while() y continua acá
    print("Cantidad de caracteres: ", contador)
    
    stream.close()
except:
    # Si en algún punto del bloque try dá error, entra acá
    print("Por algún motivo no pudo abrir el archivo...")


print("Acá continua el programa...")















