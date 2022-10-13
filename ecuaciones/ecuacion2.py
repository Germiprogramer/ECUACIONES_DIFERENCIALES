import sympy 
from ecuaciones.funciones import *
import math


def problema2():
    sympy.init_printing(use_latex='mathjax')

    x = sympy.Symbol('x')
    y = sympy.Function('y')

    f = (y(x)*(math.log(y(x)))/math.sin(x))

    print("Respuesta: ", sympy.dsolve(y(x).diff(x) - f))

    graficar2(math.pi/2)

