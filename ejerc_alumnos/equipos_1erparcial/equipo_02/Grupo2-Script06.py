# Escriba un programa que pida los coeficientes de una ecuación de segundo grado (a x² + b x + c = 0) y escriba la solución.

# Se recuerda que una ecuación de segundo grado puede no tener solución, tener una solución única, tener dos soluciones o que 
# todos los números sean solución. Se recuerda que la fórmula de las soluciones cuando hay dos soluciones 
# es x = (-b ± √(b2-4ac) ) / (2a)

# Estos son algunos ejemplos de posibles respuestas (el orden de los ejemplos no tiene por qué corresponder con el orden de las 
# condiciones).

# a	b	c	Solución
# 1	-2	2	Sin solución real
# 2	-7	3	Dos soluciones: 0.5 y 3.0
# 1	2	1	Una solución: -1.0
# 0	0	5	Sin solución
# 0	0	0	Todos los números son solución
# 0	3	2	Una solución: -0.666..


from math import sqrt

def solucion(a,b,c):
    if a == 0 and b == 0:
        print('No tiene solucion')
    elif a == 0:
        resultado = (-c/b)
        print('Tiene una sola solucion: ', resultado)
    else:
        raiz = b**2 - 4*a*c
        if raiz < 0:
            print('Sin solucion real')
        elif raiz == 0:
            resultado = -b / (2*a)
            print ('Tiene una sola solucion', resultado)
        else:
            raiz = sqrt(b**2 - 4*a*c)
            resultado1 = (-b + raiz) / (2*a)
            resultado2 = (-b - raiz) / (2*a)
            print('Tiene dos soluciones, raiz: ', resultado1 , 'y raiz:', resultado2)


# La función obtener_coeficiente se encarga de solicitar un coeficiente al usuario y repetir hasta que se ingrese un valor numérico. 
def obtener_coeficiente(nombre):
    while True:
        try:
            return float(input(f"Ingrese el coeficiente {nombre}: "))
        except ValueError:
            print(f"Error: Ingrese solo valores numéricos para el coeficiente {nombre}.")


#La función main, llama a obtener_coeficiente para cada coeficiente que necesitamos.
def main():
    print('Ingresar los coeficientes de la ecuacion de segundo grado (a x² + b x + c) \n')
    a = obtener_coeficiente('a')
    b = obtener_coeficiente('b')
    c = obtener_coeficiente('c')

    # Calcular y mostrar las soluciones 
    if a == 0 and b == 0 and c == 0:
        print('Todos los números son solucion')
    else: 
        solucion(a,b,c)
        

# --------------------------------llamado de funcion main---------------------------------

main()


# perfecto, al final funciona bien, lo había controlado mal.. Felicitaciones!




