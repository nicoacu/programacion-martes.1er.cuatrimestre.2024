

# Escribir archivos


minombre = "Juan Pablo"



directorio_trabajo = '/var/www/html/istea/infra/programacion-martes.1er.cuatrimestre.2024/unidad-11/en_clase/'

nombre_archivo = 'archivo_escritura.txt'

nombre_completo = directorio_trabajo + nombre_archivo

try:
    stream = open( nombre_completo, 'r' )
    print(stream.read())
    stream.close()

except:
    print("Hubo un error al intentar abrir el archivo...")
# stream.write("Hola mundo estoy escribiendo el archivo\n")









