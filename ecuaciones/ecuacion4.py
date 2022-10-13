import matplotlib.pyplot as plt
import numpy as np
import sympy 
from scipy import integrate

def problema4():
    sympy.init_printing(use_latex='mathjax')

    x = sympy.Symbol('x')
    y = sympy.Function('y')

    f = ((3*x**2+y(x))/(2*x))

    ec2 = sympy.Eq(y(x).diff(x), f)

    print("Respuesta: ", sympy.dsolve(y(x).diff(x) - f))

problema4()