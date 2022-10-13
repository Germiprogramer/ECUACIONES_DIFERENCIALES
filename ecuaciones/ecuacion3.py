import matplotlib.pyplot as plt
import numpy as np
import sympy 
from scipy import integrate
import math

sympy.init_printing(use_latex='mathjax')

def problema3():
    x = sympy.Symbol('x')
    y = sympy.Function('y')

    f = (2*(x-2)**2-y(x)/(x-2))

    ec2 = sympy.Eq(y(x).diff(x), f)

    print("Respuesta: ", sympy.dsolve(y(x).diff(x) - f))

problema3()