from matplotlib.pyplot import *
import math
from scipy.integrate import *
import os
import platform


def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def graficar1(x0):

    T = range(-25,25,1)


    def fun(x,y):
        return x**2*(y)-(y)/(y)+1

    solucion = odeint(fun,x0,T)

    plot(T,solucion)
    savefig('grafico1.png')
    show()

def graficar2(x0):

    T = range(-25,25,1)


    def fun(x,y):
        return (y*(math.log(y))/math.sin(x))

    solucion = odeint(fun,x0,T)

    plot(T,solucion)
    savefig('grafico2.png')
    show()

def graficar3(x0):

    T = range(-25,25,1)


    def fun(x,y):
        return (2*(x-2)**2-y/(x-2))

    solucion = odeint(fun,x0,T)

    plot(T,solucion)
    savefig('grafico3.png')
    show()

def graficar4(x0):

    T = range(-25,25,1)

    def fun(x,y):
        return ((3*x**2+y)/(2*x))
    solucion = odeint(fun,x0,T)

    plot(T,solucion)
    savefig('grafico4.png')
    show()

