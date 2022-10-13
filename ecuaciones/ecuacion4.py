import matplotlib.pyplot as plt
import numpy as np
import sympy 
from scipy import integrate
import math

sympy.init_printing(use_latex='mathjax')

x = sympy.Symbol('x')
y = sympy.Function('y')

f = ((3*x**2+y(x))/(2*x))

ec2 = sympy.Eq(y(x).diff(x), f)

print("Respuesta: ", sympy.dsolve(y(x).diff(x) - f))

respuesta = sympy.dsolve(y(x).diff(x) - f)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))