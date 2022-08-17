# Proyecto No.1, Método de Regula Falsi
# Grupo No.7:
#      Jose Block, 18935
#      Abril Palencia, 18198
# Fecha: 08/07/2022
import math
#Metodos desarrollados en clase
###############################################################################################################################
###############################################################################################################################
###############################################################################################################################

def MetodoBiseccion(func, a, b, tabla='N', tol=1E-10):
    # Evalúe los extremos del intervalo
    fa = func(a)
    fb = func(b)

    if tabla == 'S' or tabla == 'Y':  # Imprima la tabla si selecciona la opción
        print(' ')
        print('Resultados del Método de Bisección')  # Encabezado Tabla
        print(' iter       a         c          b        f(a)       f(c)       f(b)     Error aproximado')
    ErrorAprox = 100
    i = 0
    while ErrorAprox >= tol: # Empiece el ciclo for de la Bisección
        # Verifique si hay un cambio de signo entre a y b
        i = i + 1
        if fa * fb > 0:
            break  # Salga del ciclo for si no hay un cambio de signo
        xc = 0.5 * (a + b)  # Punto Medio
        ErrorAprox = abs(b - xc)
        fc = func(xc)  # Valor funcional en el punto medio
        if tabla == 'S' or tabla == 'Y':  # Imprima los resultados de cada iteración
            print(
                '{:3d}    {:8.6f}   {:8.6f}  {:8.6f}   {:8.4f}   {:8.4f}   {:8.4f}     {:5.3e}'.format(i + 1, a, xc, b,
                                                                                                       func(a),
                                                                                                       func(xc),
                                                                                                       func(b),
                                                                                                       ErrorAprox))
        if fc == 0:
            break  # Salga del ciclo for si se encuentra la raíz exacta
        # Actualice el nuevo intervalo
        if fa * fc < 0:  # El nuevo intervalo es [a xc]
            b = xc
        else:  # El nuevo intervalo es [xc xb]
            a = xc
            fa = fc  # Actualice el valor funcional del extremo izquierdo
        # fin if-else
        # Termine la iteración si el Error Aproximado es menor a una tolerancia
        if ErrorAprox < tol:
            print(' ')
            print('Se satisface la tolerancia especificada después de', i + 1, 'iteraciones.')
            break

    # fin for

    # La raiz aproximada es el punto medio del último intervalo
    xr = 0.5 * (a + b)

    # Imprima los resultados del método de Bisección
    if fa * fb > 0:
        print('El método de Bisección no encontró una raíz aproximada después de {:3d} iteraciones'.format(i + 1))
        print('El cambio de signo f(a)f(b)<0 no se satisface')
        print('--------------------------------------------------------------------')
        print(' ')
    else:
        print(' ')
        print('--------------------------------------------------------------------')
        print('Método de Bisección: Después de {:3d} iteraciones'.format(i + 1))
        print('Una raíz de f(x) se encuentra encerrada entre [{:7.5f} ,  {:7.5f}] . \n'.format(a, b))
        print('La raíz aproximada de f(x) es   {:2.7f} . '.format(xr))
        print('--------------------------------------------------------------------')
        print(' ')

    return xr, i  # El único output es la raíz aproximada


def MetodoNewton(funcion, derivada, est_inicial, tabla='N', tol=1E-10):
    xi = est_inicial  # El estimado inicial es la iteracion x0

    if tabla == 'S' or tabla == 'Y':  # Imprima la tabla si selecciona la opción
        print(' ')
        print('Iteraciones del Método de Newton')  # Encabezado Tabla
        print(' iter         xi            f(xi)      Error Aproximado ')
        # print(' iter     xi        f(xi)      df(xi)    xi+1')
    ErrorAprox = 100
    i = 0
    while ErrorAprox >= tol:
        i = i + 1
        if derivada(xi) == 0:  # Termine la iteración si la derivada es igual a cero
            break
        # Evalúe la función y la derivada en la estimación inicial
        fxi = funcion(xi)  # valor funcional
        dfxi = derivada(xi)  # Pendiente de la recta tangente
        x_ant = xi  # Valor anterior de la estimación
        xi = xi - fxi / dfxi  # Nuevo estimación de la raíz
        ErrorAprox = abs(xi - x_ant)  # Error aproximado

        # Imprima la tabla de Resultados
        if tabla == 'S' or tabla == 'Y':  # Imprima la tabla si selecciona la opción
            print('{:3d}    {:13.10f}     {:6.3e}     {:5.3e} '.format(i + 1, xi, funcion(xi), ErrorAprox))
            # print('{:3d}    {:7.4f}    {:7.4f}    {:7.4f}    {:7.4f}'.format(i+1, x_ant, fxi, dfxi, xi))
        # fin if

        if ErrorAprox < tol:
            print(' ')
            print('Se satisface la tolerancia especificada después de', i, 'iteraciones.')
            break
    
    if derivada(xi) == 0:
        print('El método de Newton no encontró una raíz aproximada después de {:3d} iteraciones'.format(i + 1))
        print('La derivada de la función es cero en x_i')
        print('--------------------------------------------------------------------')
        print(' ')
    else:
        print(' ')
        print('--------------------------------------------------------------------')
        print('Método de Newton: Después de {:3d} iteraciones'.format(i + 1))
        print('La raíz aproximada de f(x) es   {:2.12f} . '.format(xi))
        print('--------------------------------------------------------------------')
        print(' ')

    return xi, i  # El único output es la raíz aproximada

def MetodoSecante(funcion, x1, x2, iters=4, tabla='N', tol=1E-10):
    xi0 = x1  # El 1er estimado inicial es la iteracion x0
    xi1 = x2  # El 1er estimado inicial es la iteracion x0

    if tabla == 'S' or tabla == 'Y':  # Imprima la tabla si selecciona la opción
        print(' ')
        print('Iteraciones del Método de la Secante')  # Encabezado Tabla
        print(' iter         xi             f(xi)       Error Aproximado ')
        # print(' iter     xi        f(xi)      df(xi)    xi+1')
    ErrorAprox = 100
    i = 0
    while ErrorAprox >= tol:
        i = i + 1
        if funcion(xi1) - funcion(xi0) == 0:  # Termine la iteración si la secante es horizontal
            break
        # Evalúe la función y la derivada en la estimación inicial
        fxi0 = funcion(xi0)  # valor funcional en x0
        fxi1 = funcion(xi1)  # valor funcional en x1
        msec = (fxi1 - fxi0) / (xi1 - xi0)  # Pendiente de la recta secante
        xi0 = xi1  # Actualice x0 a x1
        xi1 = xi1 - fxi1 / msec  # Nueva estimación de la raíz
        ErrorAprox = abs(xi1 - xi0)  # Error aproximado
        # Imprima la tabla de Resultados
        if tabla == 'S' or tabla == 'Y':  # Imprima la tabla si selecciona la opción
            print('{:3d}    {:13.10f}      {:8.3e}      {:5.3e} '.format(i + 1, xi1, funcion(xi1), ErrorAprox))
            # print('{:3d}    {:7.4f}    {:7.4f}    {:7.4f}    {:7.4f}'.format(i+1, xi0, fxi1, msec, xi1))
        # Termine la iteración si el Error Aproximado es menor a una tolerancia
        if ErrorAprox < tol:
            print(' ')
            print('Se satisface la tolerancia especificada después de', i + 1, 'iteraciones.')
            break
        # fin if
    # fin ciclo for

    # Imprima los resultados del método de Newton
    if funcion(xi1) - funcion(xi0) == 0:  # Termine la iteración si la secante es horizontal
        print('El método de la Secante no encontró una raíz aproximada después de {:3d} iteraciones'.format(i + 1))
        print('La secante tiene pendiente horizontal entre xi+1 y xi')
        print('--------------------------------------------------------------------')
        print(' ')
    else:
        print(' ')
        print('--------------------------------------------------------------------')
        print('Método de la Secante: Después de {:3d} iteraciones'.format(i + 1))
        print('La raíz aproximada de f(x) es   {:2.12f} . '.format(xi1))
        print('--------------------------------------------------------------------')
        print(' ')

    return xi1, i
###############################################################################################################################
###############################################################################################################################
###############################################################################################################################
###############################################################################################################################









import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from sympy import *

e =math.e

print("""\n
Método de la Regla Falsa (Regula Falsi):

Es un método cerrado para encontrar las raices de una función. Este metodo toma como punto medio el cruce con el eje x 
al trazar una linea secante definida por los punto de la función en los extremos del intervalo.  Al evaluar el punto 
medio encontrado y los intervalos,  se debe escoger las funciones que den signos diferentes y descartar el otro extremo
que tenga el mismo signo.  Con estos nuevos intervalos se traza una nueva línea. Este proceso se realiza sucesivamente 
hasta llegar a la linea tangente de la función dada; por lo tanto, el punto de tangencia es la raíz.


            f(b_k)a_k - f(a_k)b_k
    c_k = -------------------------
               f(b_k) - f(a_k)


""")

#Lector de funcion
def functionLexer(fun, valor1):
    y = var('y')
    expr = sympify(fun)
    res1 = expr.subs(y, valor1)
    operadores = [
        ['suma', ' + '],
        ['Resta', ' - '],
        ['Multiplicación', ' * '],
        ['División', ' / '],
        ['Exponente', ' ** '],
        ['Raiz', ' **(0.n) '],
        ['Prioridad', ' () ']
    ]
    
    # header de la tabla
    head = ["Operación", "input"]
    print("Tabla No.1")
    print(tabulate(operadores, headers=head, tablefmt="grid"))
    print("""
    Ejemplos:
        1) x**2 + 3*x -10
        2) 7*(x**2) + x**(0.5) + 1
        3) x**4 + 3*(x**2) -5
    """)
    # if ('y' in fun):
    #     valor2 = input('Ingrese el valor de y: ')
    #     res1 = res1.subs(y, valor2)
    # if ('z' in fun):
    #     valor3 = input('Ingrese el valor de z: ')
    #     res1 = res1.subs(z, valor3)
    return float(res1)

def regula_falsi(fun, a, b, tolera=1E-10):
    print('\n\nA continuación se realizará el método de regula falsi:\n\n')
    tabla = []
    punto = abs(b-a)
    if punto == 0:
        print('Error en el rango enviado, el rango tiene longitud 0.')
    # evaluar en el punto a
    fa = fun(a)
    # evaluar en el punto b
    fb = fun(b)
    ErrorAprox = 100
    while punto >= tolera:
        # Para hallar la intersección de la recta con el eje X
        c = b - fb * (a - b ) / (fa - fb)
        # evaluar en la interseccion, c
        fc = fun(c)
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
        c
    # para saber la cantidad de iteraciones        
    ntabla = len(tabla)
    # mostrar tabla de iteraciones
    head = ["a", "c", "b", "f(a)", "f(c)", "f(b)", "margen de error"]
    print()
    print(tabulate(tabla, headers=head, tablefmt="grid"))
    print()
    # RESULTADOS
    print("Número de iteraciones: ", ntabla)
    print("Raiz: ", c)
    print("Error: ", punto)
    print()
    return c, ntabla

formulas = ["Newton Raphson", "Bisección", "Secante", "Regula Falsi"]
y = symbols("y")
fun = exp(-y) + cos(y)
fun2 = y**3 -3*y
fun3 = y**3 + 4*y**2 - 10
fundif = fun.diff(y)
fundif2 = fun2.diff(y)
fundif3 = fun3.diff(y)

def funcion(y):
    f = str(fun).replace("y", str(y))
    return float(eval(f))

def funcion2(y):
    f = str(fun2).replace("y", str(y))
    return float(eval(f))

def funcion3(y):
    f = str(fun3).replace("y", str(y))
    return float(eval(f))

def derivada(y):
    f = str(fundif).replace("y", str(y))
    return float(eval(f))

def derivada2(y):
    f = str(fundif2).replace("y", str(y))
    return float(eval(f))

def derivada3(y):
    f = str(fundif3).replace("y", str(y))
    return float(eval(f))

def methods_excercise():
    print('\n\nEjercicio 3 de la hoja de trabajo\n\n')
    regulaFalsi, itersRF = regula_falsi(funcion, 1, 2)
    newtonRaphson, itersNR = MetodoNewton(funcion, derivada, 1)
    biseccion, itersB = MetodoBiseccion(funcion, 1, 2)
    secante, itersS = MetodoSecante(funcion, 1, 2)
    results = [newtonRaphson, biseccion, secante, regulaFalsi]
    steps = [itersNR, itersB, itersS, itersRF]
    print("Tabla No.1")
    print(tabulate({'Método': formulas,'pasos':steps, 'resultados': results}, headers="keys", tablefmt='fancy_grid'))

    print('\n\nEjemplo 2\n\n')
    regulaFalsi, itersRF = regula_falsi(funcion2, 1, 3)
    newtonRaphson, itersNR = MetodoNewton(funcion2, derivada2, 3)
    biseccion, itersB = MetodoBiseccion(funcion2, 1, 3)
    secante, itersS = MetodoSecante(funcion2, 1, 3)
    results = [newtonRaphson, biseccion, secante, regulaFalsi]
    steps = [itersNR, itersB, itersS, itersRF]
    print("Tabla No.2")
    print(tabulate({'Método': formulas,'pasos':steps, 'resultados': results}, headers="keys", tablefmt='fancy_grid'))

    print('\n\nEjemplo 3\n\n')
    regulaFalsi, itersRF = regula_falsi(funcion3, 1, 2)
    newtonRaphson, itersNR = MetodoNewton(funcion3, derivada3, 2)
    biseccion, itersB = MetodoBiseccion(funcion3, 1, 2)
    secante, itersS = MetodoSecante(funcion3, 1, 2)
    results = [newtonRaphson, biseccion, secante, regulaFalsi]
    steps = [itersNR, itersB, itersS, itersRF]
    print("Tabla No.3")
    print(tabulate({'Método': formulas,'pasos':steps, 'resultados': results}, headers="keys", tablefmt='fancy_grid'))

    print('\n\nDiscusión de resultados\n\n')
    print("En las tablas de resultados se puede observar que el método de Newton-Raphson siempre tiene las iteraciones/pasos más bajos a comparación de los otros \nmétodos, esto puede ser porque el método de Newton es un método abierto y que su eficiencia es mejor en ecuaciones no lineales como las usadas en el \nproyecto. Por otro lado, el método Regula Falsi muestra una menor eficiencia porque, como se puede observar en las tablas 1 y 2, \nes el método con más iteraciones/paso hasta llegar a la tolerancia de error esperado. Esto se puede deber a que es un método cerrado, es \ndecir que depende de un intervalo a y b como el método de Bisección. También que el método Regula False bajo ciertas condiciones este tiene orden de convergencia lineal, por lo que suele converger más lentamente a la solución de la ecuación. Aunque como se puede observar en la tabla 3 el método \nde Regula Falsi realizó menos iteraciones/pasos que el método de Bisección y esto puede ser que se ingresó un intervalo más pequeño y que la ecuación dada para este ejemplo es \nmás favorable para este método en específico.")
    print('\n\nConclusiones\n\n')
    print("1. El método de Newton-Raphson es el más preciso y eficiente a comparación de los métodos de Secante, Bisección y Regula Falsi.")
    print("2. Los métodos abiertos son mas eficientes.")
    print("3. El método de Regula Falsi y Bisección son los más lentos, si las condiciones son favorables el método de Regula Falsi puede superar en eficiencia al método de Bisección.")
    print('\n\n')
methods_excercise()
