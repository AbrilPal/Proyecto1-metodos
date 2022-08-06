
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


#Biseccion

def biseccion():

    print('bisec')