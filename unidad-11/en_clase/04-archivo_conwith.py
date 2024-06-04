





# Escribir archivos


minombre = "Juan Pablo"



directorio_trabajo = '/var/www/html/istea/infra/programacion-martes.1er.cuatrimestre.2024/unidad-11/en_clase/'

nombre_archivo = 'archivo_escritura.txt'

nombre_completo = directorio_trabajo + nombre_archivo


with open(nombre_completo, 'r', encoding='utf-8') as puntero_del_archivo:
    caracteres = puntero_del_archivo.read(9)
    print(caracteres)



# acá salimos del bloque with ya lo va a cerrar automaticamente......











