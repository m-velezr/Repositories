# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 09:09:42 2023

@author: Mariana Velez
"""



def cargar_atletas(nombre)->list:
    """
    función1
    Carga la información del archivo atletas.csv y crea un diccionario 
    para cada atleta y lo guarda en una lista.
    
    Returns
    -------
    list
        lista que contiene diccionarios con la información de cada atleta en el archivo

    """
    
    atletas = []
    
    archivo= open(str(nombre)+".csv","r")
    
    encabezados = archivo.readline().strip()
    encabezados = encabezados.split(",")
    
    linea = archivo.readline().strip()
    linea = linea.split(",")
    
    
    while  linea != [""] and linea != []:
        atleta = {}
       
        for i in range(0,len(linea)):
           
           atleta[encabezados[i]]=linea[i]
           
        atletas.append(atleta)
        linea =  archivo.readline().strip()
        linea = linea.split(",")
       
    archivo.close()
   
    return atletas

        

def atletas_por_anio(atletas: list, año: int) -> dict:
    
    """ 
    función 2
    Recibe una lista y un año para buscar entre los diccionarios de la lista 
    que evento ocurrió en ese año y que atleta participó en él.
    
    Returns
    -------
    dict
        diccionario que contiene como llave el evento y como valor una lista de nombres.
    """
    diccionario ={}
    eventos = []
    
    for i in atletas:
        if i["anio"] == str(año):
            if i["evento"] not in eventos:
                eventos.append(i["evento"])
                
    for i in eventos:
        diccionario[i]= []
        
    for i in atletas:
        if i["anio"] == str(año):
            diccionario[i["evento"]].append(i["nombre"])
        
            
    return diccionario
     

    
def medallas_en_rango(atletas: list, nombre: str, anio_i: int, anio_f: str) -> list:
    """
    función 3
    Busca los atletas que ganaron medallas en un evento específico en un rango de años específico.
    
    Parameters
    ----------
    atletas : list
        lista de diccionarios que contienen información de los atletas
    nombre : str
        nombre del evento a buscar
    anio_i : int
        año inicial del rango de búsqueda
    anio_f : int
        año final del rango de búsqueda
    
    Returns
    -------
    list
        lista de diccionarios que contienen información de los atletas que ganaron medallas en el evento
        especificado en el rango de años especificado
    """
    
    lista_medallas = []
    nombre = nombre.lower()
    
    for i in atletas:
        if i["nombre"] == nombre and anio_f >= int(i["anio"]) >= anio_i:
            if i["medalla"] != "na":
                medallas = {
                    "evento": i["evento"],
                    "año": i["anio"],
                    "medalla": i["medalla"]
                }
                
            
                lista_medallas.append(medallas)
    
    return lista_medallas

def atletas_por_pais(atletas:list, pais: str)-> list:        
    """
    función 4
    
    
    Busca los atletas del país que entra por parámetro.
    
    Parameters
    ----------
    atletas : list
        lista de diccionarios que contienen información de los atletas
    país : str
        nombre del país a buscar

    Returns
    -------
    list
        lista de diccionarios que contienen información de los atletas que pertenecen al país.
    """
    
    lista_pais = []
    pais=pais.lower()
    
    for i in atletas:
        if i["pais"]==pais:
            diccionario = {
                "nombre": i["nombre"],
                "evento": i["evento"],
                "año": i["anio"]
                }
        
            lista_pais.append(diccionario)
        
    
    return lista_pais
        
def pais_con_mas_atletas(atletas: list)-> dict:
    
    """
    función 5
    Busca en la lista el país con más medallistas.
    
    Parameters
    ----------
    atletas : list
        lista de diccionarios que contienen información de los atletas
   

    Returns
    -------
    dict
        diccionario con el país que ha tenido más medallistas.
        
    
    """
   
    lista_pais=[] 
    diccionario_pais={}
     
    
    for i in atletas:
        if i["pais"] not in lista_pais:
            lista_pais.append(i["pais"])
            diccionario_pais[i["pais"]] = 0
            
        if i["medalla"] != "na":
            diccionario_pais[i["pais"]] += 1    
    
    mayor = 0
    
    for i in diccionario_pais:
       if diccionario_pais[i] > mayor:
           nombre= i
           mayor = diccionario_pais[i]
    
    respuesta={nombre: mayor}
    
    return respuesta
            
                    
    
def medallistas_por_evento(atletas: list, evento: str)->str:    
    """
    función 6
    Busca los atletas que participaron en el evento que entra por parámetro.
    
    Parameters
    ----------
    atletas : list
        lista de diccionarios que contienen información de los atletas
    evento : str
        nombre del evento a buscar

    Returns
    -------
    str
        cadena de caracteres que contiene los nombres de los atletas que participaron en el evento.
        
    """ 
    
    cadena = ""
    evento = evento.lower()
    
    for i in atletas:
        if i["evento"]==evento:
            if i["nombre"] not in cadena and cadena == "" :
                cadena += i["nombre"]
                
            if i["nombre"] not in cadena and cadena != "":
                 cadena += ","
                 cadena += i["nombre"]
           
    return cadena 
        
def atletas_con_mas_medallas_que(atletas: list, limite: int)-> dict:
    
    """
    función 7
    Busca en la lista de atletas cuantos de estos tienen una cantidad de medallas
    superior al límite

    Parameters
    ----------
    atletas : list
        lista de diccionarios que contienen información de los atletas
    limite : int
        limite inferior de medallas que deben superar los atletas.

    Returns
    -------
    dict
        Debe retornar un diccionario con el nombre de los atletas que hayan superado 
        el límite de medallas como llave y la cantidad ganada de medallas como valor.

    """
       
 
    diccionario_atletas={}
    respuesta={}
     
    
    for i in atletas:
        if i["medalla"] != "na":
            if i["nombre"] not in diccionario_atletas:
                diccionario_atletas[i["nombre"]]=0
            
            diccionario_atletas[i["nombre"]]+=1
            
       
    
    for i in diccionario_atletas:
       if diccionario_atletas[i] > limite:
           respuesta[i] = diccionario_atletas[i]
           
    return respuesta



def atleta_estrella(atletas: list)-> dict:
    """
    funcion 8
    
    Busca el atleta con mayor número de medallas ganadas

    Parameters
    ----------
    atletas : list
        lista de diccionarios que contienen información de los atletas

    Returns
    -------
    dict
        retorna un diccionario con el nombre del atleta con mayor cantidad de medallas ganadas
        en todos los años, si hay más de un atleta con las mismas medallas ganadas, se incluyen también.

    """
    
    diccionario={}
    
    
    for i in atletas:
        
        if i["medalla"] != "na":
            if i["nombre"] not in diccionario:
                diccionario[i["nombre"]]=0
                
            diccionario[i["nombre"]]+=1
        
    
    mayor = 0
    nombre = ""
    
    
    for i in diccionario:
        if diccionario[i]>mayor:
            mayor = diccionario[i]
            nombre = i
    
    respuesta= {nombre:mayor}
    
    for i in diccionario:
        if diccionario[i]==respuesta[nombre]:
            respuesta[i] = diccionario[i]
    
    return respuesta
        
def mejor_pais_en_un_evento(atletas: list, evento: str)->dict:
    """
    funcion 9
    
    Busca en un evento determinado el país que mejor desempeño haya obtenido.

    Parameters
    ----------
    atletas : list
        lista de diccionarios que contienen información de los atletas
    
    evento : str
        evento del cual se quiere saber cual fue el país con más medallistas.

    Returns
    -------
    dict
        retorna un diccionario con la llave: nombre del país con más medallistas y con el 
        valor de una lista con el número de medallas ganadas separadas por "gold, silver, bronce"

    """
    evento=evento.lower()
    ganador={}
    
    for i in atletas:
        if i["medalla"] != "na" and i["evento"]==evento:
            if i["pais"] not in ganador:
                ganador[i["pais"]]=[0,0,0]
                
            if i["medalla"] == "gold":
                ganador[i["pais"]][0] += 1
            
            elif i["medalla"] == "silver":
                ganador[i["pais"]][1] += 1
            
            elif i["medalla"] == "bronze":
                ganador[i["pais"]][2] += 1
                
    pais=""
    respuesta ={"":[0,0,0]}
    
    for i in ganador:
        lista=ganador[i]
        if lista[0]>respuesta[pais][0]:
            pais=i
            respuesta={i:lista}
        elif lista[0]==respuesta[pais][0]:
            if lista[1]>respuesta[pais][1]:
                pais=i
                respuesta={i:lista}
            elif lista[1]==respuesta[pais][1]:
                if lista[2]>respuesta[pais][2]:
                    pais=i
                    respuesta={i:lista}
                elif lista[2]==respuesta[pais][2]:
                    pais=i
                    respuesta[i]=lista
                    
                
            
            
    return respuesta     
        
            
def todoterreno(atletas:list)->str:
     """
     función 10
     
     Busca el atleta que más haya competido en eventos diferentes a través de los 
     años.

     Parameters
     ----------
     atletas : list
         lista de diccionarios que contienen información de los atletas
     

     Returns
     -------
     Retorna el nombre del atleta que más ha participado en diferentes eventos a
     lo largo de todos los años

     """
     todoterreno ={}
     mayor=0
     nombre = ""
     
     for i in atletas:  
         if i["nombre"] not in todoterreno:
             todoterreno[i["nombre"]]=[i["evento"]]
         
         if i["evento"] not in todoterreno[i["nombre"]]:
             todoterreno[i["nombre"]].append(i["evento"])
    
     for i in todoterreno:
         if len(todoterreno[i])>mayor:
             mayor = len(todoterreno[i])
             nombre = i
    
     return nombre
 
def medallistas_por_nacion_y_genero(atletas: list, pais: str, genero: str)->dict:
    """
    funcion 11

    Parameters
    ----------
    atletas : list
        lista de diccionarios que contienen información de los atletas
    pais : str
        nombre de país que entra por parámetro en el cual se deben buscar l@s 
        medallitas.
    genero : str
        genero que entra por parámetro y el cual define si se deben buscar medallistas
        mujeres u hombres en los paises

    Returns
    -------
    dict
       retorna un diccionario con los nombres de l@s atletas como llaves y como valor asigninado
       una lista que contiene varios diccionarios con la llave: evento, año y medalla
        
    """
    deportista={}
    pais=pais.lower()
    
    for i in atletas:
        if i["genero"]==genero and i["pais"]==pais and i["medalla"]!="na":
            if i["nombre"] not in deportista:
                deportista[i["nombre"]]=[]
                
            anexo={"evento":i["evento"],
                   "año":i["anio"],
                   "medalla":i["medalla"]}
            
            deportista[i["nombre"]].append(anexo)    
    
    return deportista
                
                
def porcentaje_medallistas(atletas: list)-> float:
    """
    funcion 12
    
    Calcula el porcentaje de atletas que ganaron alguna medalla


    Parameters
    ----------
    atletas : list
        lista de diccionarios que contienen información de los atletas

    Returns
    -------
    float
        retorna un decimal que será el porcentaje de medallistas.

    """            
    
    competidores=[]
    medallistas=[]
    total_competidores =0
    total_medallistas =0 
    
    for i in atletas:
        if i["nombre"] not in competidores:
            competidores.append(i["nombre"])
            total_competidores += 1
          
    
    for i in atletas:
        if i["nombre"] not in medallistas and i["medalla"]!="na":
            medallistas.append(i["nombre"])
            total_medallistas += 1
           
            
    porcentaje_medallistas = round(total_medallistas/total_competidores,2) 
    
    return porcentaje_medallistas
       
        
         
             
         
        
        
    
    
    