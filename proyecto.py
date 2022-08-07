# Proyecto No.1, Método de Regula Falsi
# Grupo No.7:
#      Jose Block, 18
#      Abril Palencia, 18198
# Fecha: 08/07/2022

# Descripcion: es un método cerrado para encontrar las raices de una función. Este metodo toma como punto medio el cruce con el eje x al trazar una
# linea secante definida por los punto de la función en los extremos del intervalo.  Al evaluar el punto medio encontrado y los intervalos,  se debe
# escoger las funciones que den signos diferentes y descartar el otro extremo que tenga el mismo signo.  Con estos nuevos intervalos se traza una 
# nueva línea. Este proceso se realiza sucesivamente hasta llegar a la linea tangente de la función dada; por lo tanto, el punto de tangencia es la raíz.

#Lector de funcion
import math
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from sympy import var
from sympy import sympify

def functionLexer(fun, valor1):
    x = var('x')
    expr = sympify(fun)
    res1 = expr.subs(x, valor1)
    # if ('y' in fun):
    #     valor2 = input('Ingrese el valor de y: ')
    #     res1 = res1.subs(y, valor2)
    # if ('z' in fun):
    #     valor3 = input('Ingrese el valor de z: ')
    #     res1 = res1.subs(z, valor3)
    return float(res1)

def regula_falsi():
    operadores = [
        ['suma', ' + '],
        ['Resta', ' - '],
        ['Multiplicación', ' * '],
        ['División', ' / '],
        ['Exponente', ' ** '],
        ['Raiz', ' **(1/n) '],
        ['Prioridad', ' () ']
    ]

    # header de la tabla
    head = ["Operación", "input"]
    print()
    print("         Tabla No.1")
    print(tabulate(operadores, headers=head, tablefmt="grid"))
    print()
    # Ingreso de la funcion, a, b y tolerancia
    fun = input('Ingresa tu funcion (guiate con la Tabla No. 1): ')
    a = float(input("Ingrese a: "))
    b = float(input("Ingrese b: "))
    tolera = float(input("Ingrese la tolerancia del error: "))

    tabla = []
    punto = abs(b-a)
    # evaluar en el punto a
    fa = functionLexer(fun,a)
    # evaluar en el punto b
    fb = functionLexer(fun,b)
    while not(punto <= tolera):
        # Para hallar la intersección de la recta con el eje X
        c = b - fb * (a - b ) / (fa - fb)
        # evaluar en la interseccion, c
        fc = functionLexer(fun,c)
        # se complio una iteracion asi que se agrega a la matriz, tabla
        tabla.append([a,c,b,fa,fc,fb,punto])
        # cambio de signo
        cambio = np.sign(fa)*np.sign(fc)
        if cambio>0:
            punto = abs(c-a)
            a = c
            fa = fc
        else:
            punto = abs(b-c)
            b = c
            fb = fc
    # para saber la cantidad de iteraciones        
    ntabla = len(tabla)

    # mostrar tabla de iteraciones
    head = ["a", "c", "b", "f(a)", "f(c)", "f(b)", "margen de error"]
    print()
    print("                                    Tabla No.2")
    print(tabulate(tabla, headers=head, tablefmt="grid"))
    print()
    # RESULTADOS
    print("Número de iteraciones: ", ntabla)
    print("Raiz: ", c)
    print("Error: ", punto)
    print()

regula_falsi()