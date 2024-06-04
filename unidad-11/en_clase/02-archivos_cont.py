

ruta_absoluta_archivo = '/var/www/html/istea/infra/programacion-martes.1er.cuatrimestre.2024/unidad-11/en_clase/archivo_ejemplo.txt'






try:
    stream = open(ruta_absoluta_archivo, "r", encoding="utf-8")
    print("El archivo se abrió correctamente")
    
    contador_lineas = 0
    contador_caracteres = 0
    linea = stream.readline()

    while linea != '':
        
        # Estoy haciendo un bucle dentro de la linea, estoy contando los caracteres
        for caracter in linea:
            contador_caracteres = contador_caracteres + 1


        print(linea, end="")
        linea = stream.readline()
        contador_lineas = contador_lineas + 1


    # En este bloque salio del while() y continua acá
    print("Cantidad de líneas: ", contador_lineas)
    print("Cantidad de caracteres: ", contador_caracteres)
    
    stream.close()
except:
    # Si en algún punto del bloque try dá error, entra acá
    print("Por algún motivo no pudo abrir el archivo...")


# print("Acá continua el programa...")















