import matplotlib.pyplot as plt
import numpy as np
import sympy 
from scipy import integrate
import math

def problema2():
    sympy.init_printing(use_latex='mathjax')

    x = sympy.Symbol('x')
    y = sympy.Function('y')

    f = (y(x)*(math.log(y(x)))/math.sin(x))

    ec2 = sympy.Eq(y(x).diff(x), f)

    print("Respuesta: ", sympy.dsolve(y(x).diff(x) - f))