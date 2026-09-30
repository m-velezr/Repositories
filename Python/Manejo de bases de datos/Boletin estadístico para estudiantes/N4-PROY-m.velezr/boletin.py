# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Boletin Estadistico
Modulo de Funciones

Temas:
* Recorridos de Matrices.
* Librerias de Matplotlib.
@author: Cupi2


"""
import csv
import pandas as pd
import matplotlib.pyplot as plt


def cargar_matriz_estadisticas(ruta_archivo: str)->list:
    """
    Esta funcion carga la informacion de la matriz de estadisticas 
    de las facultades a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con las estadisticas por facultad
    """  
    archivo = open(ruta_archivo,"r")
    linea = archivo.readline()
    facultades = 11
    elementos = 9
    estadisticas = []
    for i in range(0,facultades+1):
        estadisticas.append([0]*(elementos+1))

    i = 0;
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0,elementos+1):
            estadisticas[i][j] = datos[j].strip()
        i += 1 
        linea = archivo.readline()
    archivo.close()
    
    return estadisticas


def cargar_matriz_puestos(ruta_archivo: str)->list:
    """
    Esta funcion carga la informacion de la matriz de puestos estudiante 
    a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con los puestos estudiante de cada facultad
    """
    archivo1 = open(ruta_archivo,"r")
    linea = archivo1.readline()
    oferentes = 11
    ocupantes = 12
    puestos = []
    for i in range(0,oferentes+1):
        puestos.append([0] * (ocupantes+1))

    i = 0;
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0,ocupantes+1):
            puestos[i][j] = datos[j].strip()
        i += 1 
        linea = archivo1.readline()
    archivo1.close()
    #print(puestos)
    
    return puestos

def cargar_matriz_dobles(ruta_archivo: str)->list:
    """
    Esta funcion carga la informacion de la matriz de dobles programas 
    a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con la cantidad de estudiantes que hacen doble programa

    """
    
    archivo2 = open(ruta_archivo,"r")
    dobles=[]
    lector=csv.reader(archivo2)
   
    
    for fila in lector:
        dobles.append(fila)
   
    archivo2.close()
   
    return dobles
     
    
    
def puestos_ofrecidos_por_facultad(puestos:list, facultad:str)->int:
    """
    Esta función busca en la matriz de puestos los cupos ofrecidos para 
    los estudiantes por la facultad que entra por parámetro

    Parameters
    ----------
    puestos : list
        matriz que contiene la cantidad de puestos disponibles para estudiantes por facultad 
        y las facultades que toman los puestos.
    facultad : str
       nombre de la facultad de la cual se desea conocer los cupos

    Returns
    -------
    int
        retorna la cantidad de puestos ofrecidos por la facultad

    """    
   

    nombre=" "
    i = 1
    pos = 0
    contar = 0
    
   
    while nombre != facultad and i<len(puestos):
        if facultad.lower() == puestos[i][0].lower():
            nombre = facultad
            pos=i
        i += 1
    
    
    if nombre != facultad:
        contar = None
   
    else:
        for valores in range(1, len(puestos[pos])):
           contar += int(puestos[pos][valores])
    

    return contar
    
def puestos_ocupados_facultad(puestos:list, facultad: str)->int:
    """
    Esta función busca en la matriz de puestos ofrecidos para los estudiantes por facultad
    cuántos puestos ha ocupado la facultad que entra por parámetro.

    Parameters
    ----------
    puestos : list
        matriz que contiene la cantidad de puestos disponibles para estudiantes por facultad 
        y las facultades que toman los puestos.
    facultad : str
       nombre de la facultad de la cual se desea conocer cuantos puestos ocupan

    Returns
    -------
    int
        retorna la cantidad de puestos ocupados por la facultad

    """   
   
    nombre=" "
    i = 0
    pos_columna = 0
    contar = 0

    
    while nombre != facultad and i<len(puestos[0]):
        if facultad.lower() == puestos[0][i].lower():
            nombre = facultad
            pos_columna=i
        i += 1

    
    
    if nombre != facultad:
        contar = None
    
    else:
        for fila in range(1, len(puestos)):
            contar += int(puestos[fila][pos_columna])
   
    return contar
        
def facultad_mas_servicial(puestos:list)->tuple:
     """
     Esta función encuentra la facultad que más atiende a estudiantes
     de otras facultades.

     Parameters
     ----------
     puestos : list
         matriz que contiene la cantidad de puestos disponibles para estudiantes por facultad 
         y las facultades que toman los puestos.

     Returns
     -------
     tuple
         retorna una tupla con el nombre de la facultad más servicial y el porcentaje de estudiantes que
         atienden de otras facultades

     """       
     
     pos_columna=1
     pos_fila=1
     facultad=""
     nombre=""
     porcentajes=[]
     nombre_facultades=[]
     
    
     while pos_columna<len(puestos[0])-1:
         facultad = puestos[0][pos_columna]
         
         
   
         while nombre != facultad and pos_fila<len(puestos):
             if facultad== puestos[pos_fila][0]:
                 nombre = facultad
                 fila_facultad=pos_fila
             pos_fila += 1
         
         total_ofrecimientos = 0
         
         for valores in range(1, len(puestos[fila_facultad])):
            total_ofrecimientos += int(puestos[fila_facultad][valores])
         
         ofrecimiento_facultad = int(puestos[fila_facultad][pos_columna])
        
         ofrecimiento_otras= abs(total_ofrecimientos -  ofrecimiento_facultad)
        
         porcentaje = round(ofrecimiento_otras/total_ofrecimientos * 100, 2)
         
         porcentajes.append(porcentaje)
        
         nombre_facultades.append(nombre)   
            
         pos_columna +=1       
         
     mayor = 0
     
     for i,valor in enumerate(porcentajes):
         if valor > mayor:
             mayor = valor
             servicial=nombre_facultades[i]
    
     return (servicial, mayor)
        
     
      
def facultad_generosa(puestos:list, facultad: str, porcentaje: float)->tuple:
    """
    Esta función busca en la matriz de puestos que facultades ofrecen la misma 
    o mayor cantidad de puestos que la facultad que entra por parámetro pide según
    el porcentaje que entra.

    Parameters
    ----------
    puestos : list
        matriz que contiene la cantidad de puestos disponibles para estudiantes por facultad 
        y las facultades que toman los puestos.
    facultad : str
       nombre de la facultad de la cual se desea conocer si otras facultades logran suplir los 
       puestos que demandan
    porcentaje : float
       porcentaje de los puestos que se espera que otras facultades puedan suplir

    Returns
    -------
    tuple
        retorna una tupla con el nombre de la facultad que más puestos logra darle a la facultad 
        y al porcentaje que entra por parámetro, en caso de que no exista se retornará "No existe
        facultad"
      

    """
   
    pos_columna=0
    total_puestos_ocupados=0
    valores=[]
    nombres=[]
    
    for i,nombre in enumerate(puestos[0]):
        if nombre.lower()==facultad.lower():
            pos_columna=i
      
 
    for fila in range(1,len(puestos)):
        total_puestos_ocupados+=int(puestos[fila][pos_columna])
    
    puestos_buscados= int(porcentaje/100 * total_puestos_ocupados)
    
    for fila in range(1,len(puestos)):
        if puestos[fila][0]!=facultad and int(puestos[fila][pos_columna])>=puestos_buscados:
            valores.append(puestos[fila][pos_columna])
            nombres.append(puestos[fila][0])
    
    if len(valores) != 0:
        valor=int(valores[0])
        porcentaje_generoso= round((valor/total_puestos_ocupados)*100,2)
        facultad_generosa=nombres[0]
        
        rta=(facultad_generosa, porcentaje_generoso)
    else:
        rta=("No existe facultad generosa", 0)
    
    return rta
        
    
def autocubrimiento(puestos:list, estadistica:list)->list:
    """
    Esta función calcula los puestos ocupados por una facultad y los divide por
    los puestos que ofrece esta misma facultad. Esto lo hace para todas la facultades
    y finalmente lo agrega como una nueva columna de la matriz estadística

    Parameters
    ----------
    puestos : list
        matriz que contiene la cantidad de puestos disponibles para estudiantes por facultad 
        y las facultades que toman los puestos.
    estadistica : list
        matriz que contiene información sobre todas las facultades

    Returns
    -------
    list
        retorna la matriz estadísticas modificada.

    """
    pos_columna = 1
    puestos_ocupados = 0
    puestos_ofrecidos = 0
    iteracion_fila=1
    nombre=""
   
    estadistica[0].append("Porcentaje de autocubrimiento")
    
    while pos_columna<len(puestos[0])-1:
        facultad = puestos[0][pos_columna]
        
        for fila in range(1,len(puestos)):
            puestos_ocupados += int(puestos[fila][pos_columna])
        
        while nombre != facultad and iteracion_fila<len(puestos):
            if puestos[iteracion_fila][0]== facultad:
                nombre=puestos[iteracion_fila][0]
                pos_fila=iteracion_fila
            iteracion_fila +=1
           
        for columna in range(1,len(puestos[pos_fila])):
            puestos_ofrecidos += int(puestos[pos_fila][columna])
            
        auto=round(puestos_ocupados/puestos_ofrecidos,2)
        
        estadistica[pos_fila].append(auto)
      
        
        pos_columna+=1
    
    return estadistica
            
def doble_mas_popular(dobles:list)->tuple:
    """
    Esta función busca en la matriz dobles el doble programa
    que más alumnos tiene inscritos

    Parameters
    ----------
    dobles : list
        matriz que contiene todos los programas de la universidad
        y muestra cuantos alumnos hace doble programa con su carrera
        principal (fila) y segunda carrera (columna)

    Returns
    -------
    list
        retorna una tuple con el nombre de los dos programas y la cantidad
        de alumnos inscritos en este

    """
    iteracion=1
    buscada=""
    contar = 0 
    nombre_doble=[]
    estudiantes_doble=[]
    no_repetir=[]
   
    
    while iteracion<len(dobles):
        nombre1=dobles[0][iteracion]
        pos_columna1=iteracion
       
        
        for columna in range(1,len(dobles[0])):
            if dobles[0][columna]!=nombre1:
                nombre2=dobles[0][columna]
                pos_columna2=columna
                
                fila=1
                while fila<len(dobles) and buscada != nombre1:
                    if dobles[fila][0]==nombre1:
                        buscada=nombre1
                        pos_fila1= fila
                    fila +=1
                contar=0
                contar += int(dobles[pos_fila1][pos_columna2])
                
                fila=1
                while fila<len(dobles) and buscada != nombre2:
                    if dobles[fila][0]==nombre2:
                        buscada=nombre2
                        pos_fila2= fila
                    fila +=1
                
                contar += int(dobles[pos_fila2][pos_columna1])
                
                unicos=sorted([nombre1,nombre2])
                
                if unicos not in no_repetir:
                    no_repetir.append(unicos)
                    nombre_doble.append((nombre1+"-"+nombre2))
                    estudiantes_doble.append(contar)
    
        iteracion += 1
        
    mayor=0
    
    for valor in range(0,len(estudiantes_doble)):
        if estudiantes_doble[valor]>mayor:
            mayor=estudiantes_doble[valor]
            doble=nombre_doble[valor]
    
    
    return (doble,mayor)


def PGA__promedio(ruta_archivo:str)->None:
    
    """
    Esta función  muestra los PGA promedio de todas las facultades de la universidad
    guardados en la matriz estadísticas, ordenados de menor a mayor en un
    diagrama de barras vertical

    Parameters
    ----------
    ruta_archivo (str): la ruta del archivo que se quiere cargar

    Returns
    -------
    None
        retorna un diagrama de barras vertical
    """
     
    df=pd.read_csv(ruta_archivo)
    df=df.sort_values(by="PGA promedio")
    facultades=df.iloc[:,0]
    PGA=df["PGA promedio"]
    
    plt.bar(facultades,PGA)
    plt.title("PGA promedio por facultad")
    plt.xlabel("Facultad")
    plt.ylabel("PGA promedio")
    plt.xticks(rotation=90)
    plt.ylim(3.5,4.2)
    plt.show()
     
def puestos_usados_estudios_dirigidos(ruta_archivo:str)->None:
    """
    Esta función muestra los puestos de otras  facultades ocupados por estudios dirigidos 
    guardados en la matriz de puestos y forma un diagrama de torta.


    Parameters
    ----------
    ruta_archivo (str): la ruta del archivo que se quiere cargar

    Returns
    -------
    None
        retorna un diagrama de torta
    """
    df=pd.read_csv(ruta_archivo)
    puestos=df["Estudios Dirigidos"]
    facultades=df.iloc[:,0]
    
    puestos=puestos.plot(kind="pie", labels=facultades, title="Uso de puestos por Estudios dirigidos en las demás facultades")
    puestos.set_ylabel("")
    
    plt.show()
    
























    