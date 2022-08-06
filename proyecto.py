# Proyecto No.1, Método de Regula Falsi
# Grupo No.7:
#      Jose Block, 18
#      Abril Palencia, 18198
# Fecha: 08/07/2022

# Descripcion: es un método cerrado para encontrar las raices de una función. Este metodo toma como punto medio el cruce con el eje x al trazar una
# linea secante definida por los puntos de la función en los extremos del intervalo.  Al evaluar el punto medio encontrado y los intervalos,  se debe
# escoger las funciones que den signos diferentes y descartar el otro extremo que tenga el mismo signo.  Con estos nuevos intervalos se traza una 
# nueva línea. Este proceso se realiza sucesivamente hasta llegar a la linea tangente de la función dada; por lo tanto, el punto de tangencia es la 
# raíz.

#Lector de funcion
from sympy import var
from sympy import sympify

def functionLexer():
    x = var('x')
    y = var('y')
    z = var('z')
    print("""
    1. Sum = '+'
    2. Substract = '-'
    3. Multiply = '*'
    4. Division = '/'
    5. Power = '**'
    6. Root = '**(1/n)'
    7. Priority = '()'
    """)
    fun = input('Ingresa tu funcion basado en x, y, z: ')
    expr = sympify(fun)
    valor1 = input('Ingrese el valor de x: ')
    res1 = expr.subs(x, valor1)
    if ('y' in fun):
        valor2 = input('Ingrese el valor de y: ')
        res1 = res1.subs(y, valor2)
    if ('z' in fun):
        valor3 = input('Ingrese el valor de z: ')
        res1 = res1.subs(z, valor3)
    print(res1)
functionLexer()
