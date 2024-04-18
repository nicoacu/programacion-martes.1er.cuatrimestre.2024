# CONSIGNA - SCRIPT 6

# Escriba un programa que pida los coeficientes de una ecuación de segundo grado (a x² + b x + c = 0) y escriba la solución.
# Se recuerda que una ecuación de segundo grado puede no tener solución, tener una solución única, tener dos soluciones o que todos los números sean solución. Se recuerda que la fórmula de las soluciones cuando hay dos soluciones es x = (-b ± √(b2-4ac) ) / (2a)
# Estos son algunos ejemplos de posibles respuestas (el orden de los ejemplos no tiene por qué corresponder con el orden de las condiciones).

# a	| b | c	    Solución
# 1	|-2 | 2	    Sin solución real
# 2	|-7	| 3	    Dos soluciones: 0.5 y 3.0
# 1	| 2	| 1	    Una solución: -1.0
# 0	| 0	| 5	    Sin solución
# 0	| 0	| 0	    Todos los números son solución
# 0	| 3	| 2	    Una solución: -0.666...

import math

print("----------------------------------------------------------------------")
print("Introduce los coeficientes de una ecuación de segundo grado (ax² + bx + c = 0)")
print("----------------------------------------------------------------------")

a = int(input("Introduce el valor de a: ")) 
b = int(input("Introduce el valor de b: "))
c = int(input("Introduce el valor de c: "))
print("\n")

match a,b,c:
    case 0, if b =! 0 and c =! 0:
        print("a es igual a 0, por lo tanto no es una ecuación de segundo grado")


ecuacion_x1 = ( -b + math.sqrt((b**2) - (4*a*c)) ) / (2*a)

ecuacion_x2 = ( -b - math.sqrt((b**2) - (4*a*c)) ) / (2*a)

print("El resultado de la raiz x1 es:", ecuacion_x1)
print("El resultado de la raiz x2 es:", ecuacion_x2)

