# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 12:39:30 2023

@author: Mariana Velez
"""

import numpy as np
import matplotlib.pyplot as plt
import math

data = np.loadtxt("DatosT3.csv",skiprows=1,delimiter=",")

# Razón de crecimiento
def reg_lineal(_X,_Y):
    """
    Esta función recibe los valores que deben tomar X & Y
    para calcular y construir la matriz que permitirá encontrar los 
    coeficientes que componen la función a modelar.

    Parameters
    ----------
    _X : float
        Valores que toma X .
    _Y : float
        Valores que toma Y.

    Returns
    -------
    U : numpy.ndarray
        Valores de los coeficientes.

    """
    
    n = len(_X)
    
    
    sx = 0.0
    sx2 = 0.0
    sy = 0.0
    sxy = 0.0
    
    
    for i in range(n):
        sx += _X[i]
        sx2 += _X[i]**2
        sy += _Y[i]
        sxy += _X[i]*_Y[i]
        
   
    A = np.array([[n,sx],
                  [sx,sx2]])
    
    b = np.array([[sy],
                  [sxy]])
    
    U = np.linalg.solve(A,b)
    
    return U


X = data[:,0]
Y = data[:,1]


def RC(X,Y):
    """
    Esta función linealiza la razón de crecimiento para
    poder calcular los coeficientes reales de la regresión 

    Parameters
    ----------
    X : float
        Valores de X que llegan desde un archivo con datos.
    Y : float
        Valores de X que llegan desde un archivo con datos.

    Returns
    -------
    float
      Retorna los coeficientes reales que debe tener la función con la que se graficará
      la regresión lineal

    """
    Yp = 1/Y
    Xp = 1/X
    a0,a1 = reg_lineal(Xp,Yp)
    alpha = 1/a0
    beta = alpha*a1
    return (alpha[0],beta[0])

alpha, beta  = RC(X,Y)

def fr_rl(x):
    """
    Esta función recibe los valores que toma X de acuerdo con los valores
    originales que se extraen del archivo y se encuentran los valores que toma
    Y una vez se utiliza la función que se encontró para la regresión lineal

    Parameters
    ----------
    x : float
        Valores de X que llegan desde un archivo con datos.

    Returns
    -------
    float
        Retorna los valores que toma Y con la regresión lineal.

    """
    y = alpha*x/(beta+x)
    return y


def R2(Y_original,Y_ajuste):
    """
    Esta función calcula el error asociado a la
    cercanía de la regresión encontrada respecto a 
    los valores originales que toma Y.

    Parameters
    ----------
    Y_original : float
        Valores originales que toma Y
    Y_ajuste : float
        Valores en Y que toma la regresión calculada

    Returns
    -------
    float
        Retorna el error 

    """
    st = 0.0
    sr = 0.0
    n = len(Y_ajuste)
    yb = np.average(Y_original)
    for i in range(n):
        st += (Y_original[i] - yb)**2
        sr += (Y_original[i] - Y_ajuste[i])**2
    return  (st-sr)/st




Y_ajuste_rl = fr_rl(X)
r2_rl = R2(Y,Y_ajuste_rl)
print("Coeficientes para la regresión lineal con razón de crecimiento:"+str(alpha) + "  &  " + str(beta))





# Mínimos cuadrados
def min_cuadrado(X):
    """
    Esta función utiliza la Formulación General, en 
    donde reemplaza las expresiones más complejas por
    z0, z1 y z2 de tal manera que se evalúan los valores de x 
    en z0, z1 y z2 para formar la matriz Z para posteriormente encontrar
    el valor de las constantes.
    
    Parameters
    ----------
    X : float
        Valores de X que llegan desde un archivo con datos.

    Returns
    -------
    Z : numpy.ndarray
        matriz (len(X)x3).
        

    """
    Z = np.zeros((len(X),3))
    
    for i in range(len(X)):
       z0 = 1
       z1 = X[i]**(1/2)
       z2 = math.log(X[i])
       Z[i,0] += z0
       Z[i,1] += z1
       Z[i,2] += z2
    
    A = Z.T @ Z
    b = Z.T @ Y
    a = np.linalg.solve(A, b)

    a0 = a[0]
    a1 = a[1]
    a2 = a[2]

    return (a0,a1,a2)



def fmin_cuad(X,a0,a1,a2):
    """
    Esta función calcula el comportamiento de la regresión lineal para 
    cada uno de los valores que toma X una vez ya se conocen los valores de 
    las constantes del polinomio.

    Parameters
    ----------
    X : float
        Valores de X que llegan desde un archivo con datos.

    Returns
    -------
        float
        Retorna los valores en Y que se obtienen con la regresión lineal.

    """
    return a0 + a1*X**(1/2)+ a2*np.log(X)

a0,a1,a2 = min_cuadrado(X)
fmin_cuad = fmin_cuad(X,a0,a1,a2)   
r2_mincuad= R2(Y,fmin_cuad) 
print("Coeficientes para la regresión lineal con mínimos cuadrados: "+str(a0)+" , " + str(a1)+"  &  " + str(a2))



plt.plot(X,Y,"o",color="k",label="Datos")
plt.plot(X,Y_ajuste_rl,"--",c="red",label=f"RL Razón de Crecimiento: {r2_rl:.3f}")
plt.plot(X,fmin_cuad,"--",c="blue",label=f"RL Mínimos Cuadrados: {r2_mincuad:.3f}")
plt.grid()
plt.title("Regresión Lineal ")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

def trapecio(X,Y):
    """
    Esta función usa la regla del trapecio para encontrar la integral
    de los datos que entran por parámetro.

    Parameters
    ----------
    X : float
        Valor en X que toma cada punto
    Y : float
        Valor en Y que toma cada punto

    Returns
    -------
    area : float
        Valor de la integral que se encuentra para tdoos los puntos que entran por parámetro

    """
    area = 0.0
    n = len(X)
    
    for i in range(0,n-1):
        area += (X[i+1] - X[i])/2*(Y[i]+Y[i+1])
        
    return area

def simpson(X,Y):
    """
    Esta función usa la regla de Simpson para encontrar la integral
    de los datos que entran por parámetro.

    Parameters
    ----------
    X : float
        Valor en X que toma cada punto
    Y : float
        Valor en Y que toma cada punto

    Returns
    -------
    area : float
        Valor de la integral que se encuentra para tdoos los puntos que entran por parámetro

    """
    
    n = len(X)
    
    if n%2 == 0:
        area = 0.0
        for i in range(0,n-4,2):
            s13 = (X[i+2]-X[i])/6 * (Y[i]+4*Y[i+1]+Y[i+2])
            area += s13
        s38 = (X[-1]-X[-4])/8 * (Y[-1]+3*Y[-2]+3*Y[-3]+Y[-4])
        area += s38
        
    if n%2 != 0:
        area = 0.0
        for i in range(0,n-2,2):
            s13 = (X[i+2]-X[i])/6 * (Y[i]+4*Y[i+1]+Y[i+2])
            area += s13
    
    return area

def gauss_legendre(a,b,n,FUNCION):
    """
    Esta función usa el método de Gauss-Legendre para calcular el área
    de la regresión lineal con razón de crecimiento 

    Parameters
    ----------
    a : float
        Valor inicial en X de los datos
    b : float
        Valor final en X de los datos
    n : int
        Número de puntos con el que se realiza el método


    Returns
    -------
    area : float
        Retorna el valos del área encontrada por el método

    """
    
    Z,W = np.polynomial.legendre.leggauss(n)
    suma = 0.0
    
    jacobiano = (b-a)/2
    
    for i in range(n):
        X = (b+a)/2 + (b-a)/2*Z[i]
        g = FUNCION(X)*W[i]
        suma += g
    
    area = suma * jacobiano
    
    return area
        
   
    
    
    
valor_x = np.linspace(X[0],X[-1],100)
print("Simpson (100): "+str(simpson(valor_x,fr_rl(valor_x))))      
print("Trapecio (100): "+str(trapecio(valor_x,fr_rl(valor_x))))             
print("Gauss-Legendre (10): "+str(gauss_legendre(X[0], X[-1],10, fr_rl)) )

valor_x = np.linspace(X[0],X[-1],59)
print("Simpson (59): "+str(simpson(valor_x,fr_rl(valor_x))))             

print("Simpson (datos): " + str(simpson(X,Y)))
print("Trapecio (datos): " + str(trapecio(X,Y)))





             
             
            
    


    


       