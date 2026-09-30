# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 13:47:53 2023

@author: Mariana Velez
"""

import numpy as np
import matplotlib.pyplot as plt


y1 = 4.32
v1 = 1.25
g = 9.81


def f(y2, dz):
    """
    Por medio de esta función se puede identificar los valores que toma la ecuación 
    dado un valor para y2 y dz.
    ----------
    y2 : float
        altura del canal angosto.
    dz : float
        variación del nivel de fondo del canal
    

    Returns
    -------
    Retorna el valor de la ecuación de Bernoulli para cada valor que toma y2 y dz.

    """
    a =  v1**2/(2*g)
    b = (v1*y1)**2/(y2**2*2*g)
    return a + y1 - b - dz - y2


# a continuación se encuentra graficamente la primera raíz del problema
x = np.linspace(-1, -0.5, 150)
y = f(x,1.05)
plt.plot(x,y)
plt.title("Primera raíz")
plt.ylabel("y")
plt.xlabel("x")
plt.axhline(0, color='red', linewidth=1)
plt.grid()
plt.show()


# De acuerdo con la gráfica anterior se identifica la primera raíz, y se establece
# un rangode búsqueda de la raíz en [-0.7,-0.6]. Los siguientes parámetros se utilizan 
# para encontrar el valor que debe tomar y2 según los valores que da el enunciado

tol=10**-8
xl = -0.7
xu = -0.6
dz= 1.05



def biseccion(FUNCION,xl,xu,dz):
    
    """
    Esta función pretende encontrar el valor más cercano las raices de la ecuación
    utilizando el método de bisección en el intervalo previamente establecido.

    Parameters
    ----------
    xl : float
        Es el valor inicial que se toma para el intervalo de búsqueda de la raíz
    
    xu : float
        Es el valor final que se toma para el intervalo de búsqueda de la raíz
    
    dz : float
        Es el valor que toma dz, este puede variar o estar fijo 

    Returns
    -------
    primera_raiz : float
        Valor aproximado que debe tomar y2 para que la ecuación de bernoulli se cumpla,
        dados los valores que se informan en el enunciado y el valor que tome dz.
    """
    if FUNCION(xl,dz)*FUNCION(xu,dz)<0:
        #cumple condición, posible raíz
        for i in range(100):
            xr = (xl+xu)/2
            if FUNCION(xr,dz)*FUNCION(xl,dz)<0:
               xu=xr
            else:
               xl = xr
            
            xr_i1=(xl+xu)/2
            error_encontrado= abs((xr-xr_i1)/xr_i1)
            if  error_encontrado <= tol:
                break
        raiz = xr_i1
        return raiz


primera_raiz = biseccion(f,-0.7, -0.6, dz)

def h(x,dz):
    """
    Por medio de esta función se encuentra la segunda raíz usando división sintética

    Returns
    -------
    retorna la segunda raíz


    """
    return f(x,dz)/(x-primera_raiz)

segunda_raiz = biseccion(h,0.01,2,1.05)


def k(x,dz):
    """
    Por medio de esta función se encuentra la segunda raíz usando división sintética

    Returns
    -------
    retorna la tercera raíz

    """
    return h(x,dz)/(x-segunda_raiz)

tercera_raiz = biseccion(k,1,10,1.05)


raices = (primera_raiz, segunda_raiz, tercera_raiz)
print("Método de bisección:")
print(raices)

def variacion_dz(XL = 1.6, XU = 3.8):
    """
    Esta función permite graficar deltaZ vs y2, en donde dz varía
    entre 0.5 a 2.2

    Parameters
    ----------
    XL : float
        Es el valor inicial que se toma para el intervalo de búsqueda de la raíz
    XU : float
        Es el valor final que se toma para el intervalo de búsqueda de la raíz

    Returns
    -------
    None.

    """
    DZ = np.linspace(0.5, 2.2, 100)
    Y2 = []

    for i in range(len(DZ)):
        dz = DZ[i]
        y2 = biseccion(f,XL,XU,dz)
        Y2.append(y2)
    plt.plot(DZ,Y2)
    plt.title(r"$\Delta z$ vs $y2$")
    plt.grid()
    plt.ylabel("y2")
    plt.xlabel(r"$\Delta z$")
    plt.show()
variacion_dz()

def df(y2):
    """
    Retorna la derivada de la ecuación de Bernoulli 

    Parameters
    ----------
    y2 : float
        DESCRIPTION.

    Returns
    -------
    Derivada con respecto a y2 de la ecuación de ber

    """
    return -1+v1**2*y1**2/(g*y2**3)
    
def newton_raphson(xi:float):
    """
    Mediante esta función se pretende encontrar las mismas tres raíces encontradas por 
    el método de bisección.

    Parameters
    ----------
    xi : float
        Valor arbitrario que se elige para acercarse a la raíz real.

    Returns
    -------
    xim1 : float
       Valor aproximado de la raíz real .

    """
     
    dz = 1.05
    
    for i in range (100):
        xim1 =  xi - f(xi,dz)/df(xi)
        error_encontrado= abs((xi-xim1)/xim1)
       
        if error_encontrado > tol:
            xi = xim1
            
        else:
            break
            
         

    return xim1

print("Método de Newton-Raphson:")
n1= newton_raphson(-1)
n2= newton_raphson(0.5)
n3= newton_raphson(3)

print((n1,n2,n3))


