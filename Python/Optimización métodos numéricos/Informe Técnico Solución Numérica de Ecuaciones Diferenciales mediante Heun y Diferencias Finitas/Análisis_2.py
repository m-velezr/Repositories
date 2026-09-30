# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 08:53:21 2023

@author: Mariana Velez
"""
import numpy as np
import matplotlib.pyplot as plt


def dif_finitas():
    """
    Esta función utiliza la diferencias finitas centradas
    para resolver una ecuacion diferencial parcial a través 
    de un sistema de ecuaciones previamente establecido.

    Returns
    -------
    Valores que toma la temperatura sobre diferentes puntos de la placa.

    """

    k = 385
    beta = 25
    t=0.001
    b=0.005
    A=t*b
    P = 2*(t+b)
    L=0.1
    n=123
    dx = L/(n-1)
    Ta = 20
    U0 = 85
    
    alpha = -k*A/(dx**2)
    sigma = beta*P - 2*alpha
    phi = alpha*dx*beta/k
    
# MA hace referencia a la matriz que se construye a partir del sistema de ecuaciones
    MA = np.diag([sigma]*(n-1)) + np.diag([alpha]*(n-2),1) + np.diag([alpha]*(n-2),-1)
    
    MA[-1,-1]= sigma-phi
    MA[-1,-2]=2*alpha
    
    c = beta*P*Ta
# F hace referencia al vector resultante 
    F = np.zeros(n-1) + c
    F[0] = c-alpha*U0
    F[-1] = Ta*(beta*P-phi)
    
# U representa la temperatura en los nodos definidos sobre la barra   
    U = np.linalg.solve(MA,F)
    U = [U0] + U.tolist()
    X = np.linspace(0,L,n)
    
    
    
    plt.plot(X,U)
    plt.title("Temperatura en diferentes puntos a lo largo de la placa")
    plt.ylabel("Temperatura (°C)")
    plt.xlabel("Longitud de la barra (m)")
    plt.grid()
    plt.savefig("Dif fin")
    
    return U

Valores_T = dif_finitas()
print(Valores_T)