# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:57:55 2023

@author: Mariana Velez
"""
import numpy as np
import matplotlib.pyplot as plt


def crout(A,b):
    """
    Esta función recibe una matriz A (nxn) y un vector b (nx1)
    y por medio del método de crout descompone la matriz A en LU, 
    de tal forma que se pueda realizar una sustitución hacia adelante y 
    posteriormente una sustitución hacia atrás para encontrar el vector x (nx1).

    Parameters
    ----------
    A : numpy.ndarray
        matriz (nxn).
    b : numpy.ndarray
        vector (nx1).

    Returns
    -------
    Vector x (nx1)

    """

    n = len(A)
    y = np.zeros(n)
    x = np.zeros(n)
    L = np.zeros((n,n))
    U = np.identity(n)
    
    
    
    for i in range(n):
        L[i,0] = A[i,0]
        U[0,i]=A[0,i]/L[0,0]
    
    j = 1
    
    while j< n-1 :
        
        for i in range(1,n):
            suma1=0.0
            suma2=0.0
            for k in range(0,j):
                suma1 += L[i,k]*U[k,j] 
            L[i,j] = A[i,j]-suma1
        
        m = j+1
        if  m < n:
         for r in range(0,j):
             suma2 += L[j,r]*U[r,m] 
                    
         U[j,m]=(A[j,m]-suma2)/L[j,j]
        
        j += 1
        
        
            
    g = n-1
    suma3=0.0
    for v in range(0,g):
        suma3 += L[g,v]*U[v,g]
                            
    L[g,g]= A[g,g]-suma3
 
#Sustitución hacia adelante
    
    for i in range(n):
        suma = 0.0
        for k in range(0,i):
            suma += L[i,k]*y[k]
        y[i]=(b[i]-suma)/L[i,i]
        
#Sustitución hacia atrás
    
    for i in range(1,n+1):
        suma=0.0
        for j in range(-i+1,0):
            suma += U[-i,j]*x[j]
        
        x[-i]=(y[-i]-suma)/U[-i,-i]
        
    return x



A = np.array([[-225,25,0,0],
              [225,-275,50,0],
              [0,220,-245,25],
              [0,30,95,-175]])

b = np.array([-2400,-2000,0,-100])

print(crout(A,b))


def f(x,y):
    
    return -((x**2+y-11)**2+ (x+y**2-7)**2-20)


def SD(f,xl,xu,n=100,tol=1e-8):
    """
    Esta función sigue el algoritmo del método de la 
    Sección Dorada para encontrar el máximo de de una función
    de una sola variable.

    Parameters
    ----------
    f : función
        Llama a la función con la que debe trabajar el método.
    xl : float
        Es el valor inicial que se toma para el intervalo de búsqueda del óptimo.
    xu :  float
        Es el valor final que se toma para el intervalo de búsqueda del óptimo.
    n : int
        Número de iteraciones para encontrar el óptimo de la función. The default is 100.
    tol : int
        La tolerancia elegida para determinar si la diferencia entre la nueva iteración
        y la anterior es aceptable. The default is 1e-8.

    Returns
    -------
    x : float
        óptimo de la función que entra por parámetro y se encuentra entre xl y xu definidos.

    """
    
    
    
    for i in range(n):
        d = (5**(1/2)-1)/2 * (xu-xl)
        x1 = xl + d
        x2 = xu - d
        
        
        if f(x2)>f(x1):
            xopt = x2
            xl = xl
            xu = x1
            x1 = x2
        
        else:
            xopt = x1
            xl = x2
            xu = xu
            x2 = x1
            
        
        errorcito = 0.3819* abs((xu-xl)/xopt) 
        
        if errorcito<tol:
            break
        x = xopt
        
    

    return x



def univariada(tol=1e-8, n = 4):
    """
    Esta función fija una variable mientras optimiza la otra,
    una vez se encuentra la nueva variable optimizada, esta se fija 
    con el fin de seguir optimizar la otra variable.
    Cuando el error de ambas variables sea menor a la tolerancia se 
    han encontrado los valores acertados para representar al óptimo.

    Parameters
    ----------
   tol : int
       La tolerancia elegida para determinar si la diferencia entre la nueva iteración
       y la anterior es aceptable. The default is 1e-6.
   n : int
        Número de iteraciones para encontrar el óptimo de la función. The default is 30.
       
    Returns
    -------
    xopt: float
        La coordenada x del óptimo de la función.
        
    yopt: float
        La coordenada y del óptimo de la función.

    """
    y = 4
    x = 2.5
    plt.plot([x],[y],"o",c="k")
   
    for i in range(n):
        
        def fyk(x):
            return f(x,y)
            
        x1= SD(fyk,-6, 6)
        plt.plot([x,x1],[y,y],"-o",c="k")
        errorx= abs((x1-x)/x1)
        
    
        def fxk(y):
            return f(x1,y)
        
        y1= SD(fxk,-6, 6)
        plt.plot([x1,x1],[y,y1],"-o",c="k")
        errory= abs((y1-y)/y1)
    
        if errory>tol or errorx>tol:
            x = x1
            y = y1
            
        
        else:
            break
    
    xopt = x1
    yopt = y1
    
    
    
    return (xopt,yopt)


#Gráfica de la función f(x,y) con la secuencia de valores que toman X y Y
#hasta encontrara el óptimo
_X = []
_Y = []
_Z = []


domx = np.linspace(-6,6,30)
domy = np.linspace(-6,6,30)

for i in range(30):
    for j in range(30):
        x = domx[i]
        y = domy[j]
        z = f(x,y)
        
        _X.append(x)
        _Y.append(y)
        _Z.append(z)
plt.tricontourf(_X,_Y,_Z, cmap="rainbow")
plt.title("Secuencia de optimización")
plt.colorbar()


print(univariada()) 
plt.show()   






