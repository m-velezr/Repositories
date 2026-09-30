# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:05:03 2023

@author: Mariana Velez
"""

import numpy as np
import matplotlib.pyplot as plt


def Heun(C1, C2, h, n):
    """
    Esta función utiliza el método de Heun para
    determinar la velocidad y distancia recorrida
    por las dos masas.

    Parameters
    ----------
    C1 : float
        Constante de amortiguamiento del primer resorte
    C2 : float
        Constante de amortiguamiento del segundo resorte
    h : float
        Tamaño de paso
    n : int
        Número de iteraciones

    Returns
    -------
    Retorna una lista con los valores de la velocidad (b) y la distancia (a).

    """
    R2 = 3000
    R1 = 3000
    M1 = 200
    M2 = 200
    
# b corresponde a la velocidad
# a corresponde a la distancia    
    
    def g(t):
        """
        Esta función calcula el valor de y para la ecuación descrita
        en el Punto 1

        Parameters
        ----------
        t : int
            tiempo

        Returns
        -------
        float
            valor que toma (y) o g(t) de acuerdo al tiempo

        """
        return np.sin(2 * np.pi * t) * 10 * (t < 15)
    
    def da1dx(x,a1,b1):
        """
        Esta función calcula el valor de la velocidad para la masa 1  usando 
        la primera derivada de la distancia respecto al tiempo

        Parameters
        ----------
        x : int
            tiempo
        a1 : float
            distancia recorrida por la masa 1
        b1 : float
            velocidad recorrida por la masa 1

        Returns
        -------
        b1 : float
            velocidad recorrida por la masa 1

        """
        return b1
    
    def db1dx(x,a1,a2,b1,b2):
        """
        Esta función calcula el valor de la aceleración alcanzada por la masa 1  
        usando la primera derivada de la velocidad para la masa 1 respecto al tiempo

        Parameters
        ----------
        x : int
            tiempo
        a1 : float
            distancia recorrida por la masa 1
        a2 : float
            distancia recorrida por la masa 2
        b1 : float
            velocidad recorrida por la masa 1
        b2 : float
            velocidad recorrida por la masa 2

        Returns
        -------
        float
            aceleración alcanzada por la masa 1

        """
        return ((a2-a1)*R2 - a1*R1 + (b2-b1)*C2 - b1*C1)/M1 + g(x)
    
    
    def da2dx(x,a2,b2):
        """
        Esta función calcula el valor de la velocidad para la masa 2  usando la 
        primera derivada de la distancia recorrida por la masa 2 respecto al tiempo.

        Parameters
        ----------
        x : int
            tiempo
        a2 : float
            distancia recorrida por la masa 2
        b2 :float
            velocidad recorrida por la masa 2

        Returns
        -------
        b2 : float
            velocidad recorrida por la masa 2

        """
        return b2
    
    def db2dx(x,a1,a2,b1,b2):
        """
        Esta función calcula el valor de la aceleración alcanzada por la masa 2 usando 
        la primera derivada de la velocidad para la masa 2 respecto al tiempo

        Parameters
        ----------
        x : int
            tiempo
        a1 : float
            distancia recorrida por la masa 1
        a2 : float
            distancia recorrida por la masa 2
        b1 : float
            velocidad recorrida por la masa 1
        b2 : float
            velocidad recorrida por la masa 2

        Returns
        -------
        float
            aceleración alcanzada por la masa 2

        """
        return (-(a2-a1)*R2 - (b2-b1)*C2)/M2 + g(x)
    
    
    
    xi = 0.0
    a1 = 0.0
    a2 = 0.0
    b1 = 0.0
    b2 = 0.0
    h = 0.02
    n = 3000
    
    X = []
    A1 = []
    A2 = []
    B1 = []
    B2 = []
    
    for i in range(n):
        
        xip1 = xi+h
        
        k1a1 = da1dx(xi,a1,b1)
        k1a2 = da2dx(xi,a2,b2)
    
        k1b1 = db1dx(xi,a1,a2,b1,b2)
        k1b2 = db2dx(xi,a1,a2,b1,b2)
        
        k2a1 = da1dx(xi + h, a1 + k1a1*h, b1 + k1b1*h)
        k2a2 = da2dx(xi + h, a2 + k1a2*h, b2 + k1b2*h)
        
        k2b1 = db1dx(xi + h, a1+k1a1*h, a2 + k1a2*h, b1 + k1b1*h, b2 + k1b2*h)
        k2b2 = db2dx(xi + h, a1+k1a1*h, a2 + k1a2*h, b1 + k1b1*h, b2 + k1b2*h)
        
        
        phia1 = (k1a1 + k2a1)/2
        phia2 = (k1a2 + k2a2)/2
        
        phib1 = (k1b1 + k2b1)/2
        phib2 = (k1b2 + k2b2)/2
        
        a1p1 = a1 + phia1*h
        a2p1 = a2 + phia2*h
        
        b1p1 = b1 + phib1*h
        b2p1 = b2 + phib2*h
        
        a1 = a1p1
        a2 = a2p1
        
        b1 = b1p1
        b2 = b2p1
        
        xi = xip1
        
        A1.append(a1)
        A2.append(a2)
        B1.append(b1)
        B2.append(b2)
        X.append(xi)

    plt.plot(X,A1, label= "Distancia")
    plt.plot(X,B1, label="Velocidad")
    plt.legend()
    plt.xlabel("Tiempo (seg)")
    plt.ylabel("Longitud (m)")
    

    plt.title("Velocidad y Distancia recorrida por los cuerpos")
    plt.show()
    
    return (A1,A2,B1,B2)
         

valor1 = Heun(0.0,0.0,0.02,3000)
valor2 = Heun(100.0,100.0,0.02,3000)
valor3 = Heun(1000,1000,0.02,3000)




















