from matplotlib.pyplot import *
import numpy as np
import sympy 
from scipy.integrate import *
import math

def graficar1(x0):

    T = range(-25,25,1)


    def fun(x,y):
        return x**2*(y)-(y)/(y)+1

    solucion = odeint(fun,x0,T)

    plot(T,solucion)
    show()

graficar1(1)