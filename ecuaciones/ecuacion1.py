
import matplotlib.pyplot as plt
import numpy as np
import sympy 
from scipy import integrate
from ecuaciones.funciones import graficar1

sympy.init_printing(use_latex='mathjax')

x = sympy.Symbol('x')
y = sympy.Function('y')
 
def problema1(x0):
    ics = {y(3): -1}

    f = (x**2*(y(x))-(y(x)))/((y(x))+1)
    print("Ecuación1: " ,sympy.Eq(y(x).diff(x), f))

    #solucion inicial
    ec1 = sympy.Eq(y(x).diff(x), f)

    C_eq = sympy.Eq(ec1.lhs.subs(x, 3).subs(ics), ec1.rhs.subs(x, 3))

    #respuesta

    print("Respuesta: ", sympy.solve(C_eq))

    graficar1(x0)






