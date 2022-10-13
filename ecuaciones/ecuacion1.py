
import matplotlib.pyplot as plt
import numpy as np
import sympy 
from scipy import integrate

sympy.init_printing(use_latex='mathjax')

x = sympy.Symbol('x')
y = sympy.Function('y')

ics = {y(3): -1}

f = (x**2*(y(x))-(y(x)))/((y(x))+1)
print("Ecuación1: " ,sympy.Eq(y(x).diff(x), f))

ec1 = sympy.Eq(y(x).diff(x), f)

C_eq = sympy.Eq(ec1.lhs.subs(x, 3).subs(ics), ec1.rhs.subs(x, 3))
print(C_eq)

#respuesta

print("Respuesta: ", sympy.dsolve(y(x).diff(x) - f))




