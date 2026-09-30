import time
import csv
csv.field_size_limit(2147483647)
import json
from datetime import datetime
from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as lt

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {"movie_title": None,
               "movie_order":None,
               "ID":None,
               "movie_idioma": None}
    
    catalog["movie_title"] = mp.new_map(45032,0.7)
    catalog["movie_order"] = mp.new_map(45032,0.7)
    catalog["ID"] = mp.new_map(45032,0.7)
    catalog["movie_idioma"] = mp.new_map(45032,0.7)
    catalog["movie_status"] = mp.new_map(45032,0.7)
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    num = 1
    for movie in input_file:
        if movie["genres"] != "[]":
            genres = movie["genres"].replace("'",'"')
            genres = json.loads(genres)
            movie["genres"] = genres
        else :
            movie["genres"] = "Indefinido"
        
        if movie["production_companies"] != "[]":
            prod = movie["production_companies"].replace("'",'"')
            prod = json.loads(prod)
            movie["production_companies"] = prod
            
        else:
            movie["production_companies"] = "Indefinido"
        
        
        if movie["revenue"] != "0" and movie["budget"] != "0" :
            movie["ganancias"] = int(movie["revenue"]) - int(movie["budget"] )
        else:
            movie["ganancias"] = "Indefinido"
        
        mp.put(catalog["movie_title"], movie["title"],movie)
        mp.put(catalog["movie_order"], num ,movie)
        mp.put(catalog["ID"], movie["id"] ,movie)
        mp.put(catalog["movie_idioma"],movie["original_language"],movie)
        mp.put(catalog["movie_status"],movie["status"],movie)
        num += 1
    size = num
    print(mp.get(catalog["movie_title"], "The Verdict"))
    #print(mp.get(catalog["movie_idioma"], "nl"))
    return size

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    rta = mp.get(catalog["ID"],id)
    return rta


def req_1(catalog,nombre,idioma):
    """
    Retorna el resultado del requerimiento 1
    """
    info = mp.get(catalog["movie_title"],nombre)
    lista = []
    if info != None:
        if isinstance(info, list): 
            for i in range(0, len(info)):
                if idioma == info[i]["original_language"]:
                    lista.append(info[i])
                    
            
        else:
            if idioma == info["original_language"]:
                    lista.append(info)
            
                    
    return lista


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog, idioma, fecha_i , fecha_f):
    
    info = mp.get(catalog["movie_idioma"],idioma)
    lista = {"elements":[],"size":0}
    if info != None:
        if isinstance(info, list): 
            for i in range(0, len(info)):
                if fecha_i <= info[i]["release_date"] <= fecha_f:
                    lista["elements"].append(info[i])
                    lista["size"] += 1
        else:
            if fecha_i <= info["release_date"] <= fecha_f:
                lista["elements"].append(info)
                lista["size"] += 1            
    return lista

def req_4(catalog, fecha_i , fecha_f , estado):
    """
    Retorna el resultado del requerimiento 4
    """
    info = mp.get(catalog["movie_status"],estado)
    lista = {"elements":[],"size":0}
    if info != None:
        if isinstance(info, list): 
            for i in range(0, len(info)):
                if fecha_i <= info[i]["release_date"] <= fecha_f:
                    lista["elements"].append(info[i])
                    lista["size"] += 1
        else:
            if fecha_i <= info["release_date"] <= fecha_f:
                    lista["elements"].append(info)
                    lista["size"] += 1            
    return lista


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog,idioma,fech_inf, fech_sup):
    """
    Retorna el resultado del requerimiento 6
    """
   
    info = mp.get(catalog["movie_idioma"],idioma)
    rta = [["Año","Total","Promedio votación promedio","Tiempo promedio duración","Ganancia acumulada","Mejor","Peor"]]
    
    if info != None:
        for j in range(fech_inf,fech_sup+1,1):
            lista=[]
            total = 0
            vot = 0
            tiempo = 0
            ganancias = 0
            mejor = 0
            peor = 1000000
            for i in range(0,len(info)):
                fecha = datetime.strptime(info[i]["release_date"], "%Y-%m-%d")
                fecha = fecha.year
                
                if j == fecha and info[i]["status"] == "Released":
                    total += 1
                    vot += float(info[i]["vote_average"])
                    tiempo += float(info[i]["runtime"])
                    ganancias += float(info[i]["runtime"] )
                    
                    if mejor<= float(info[i]["vote_average"]):
                        mejor = float(info[i]["vote_average"])
                        nombre_m = info[i]["title"]
                    
                    if peor >= float(info[i]["vote_average"]):
                        peor = float(info[i]["vote_average"])
                        nombre_p = info[i]["title"]
                        
            
            vot_prom = round(vot/total,2)  
            tiempo_prom =  round(tiempo/total,2)  
            mejor_peli = {nombre_m:mejor}
            peor_peli = {nombre_p:peor}
            lista = [j, total, vot_prom, tiempo_prom, ganancias, mejor_peli, peor_peli]
            rta.append(lista)
              
               
                        
                        
        return rta
        
        
    else:
        return None
            

def req_7(catalog, year_i, year_f,productora ):
    """
    Retorna el resultado del requerimiento 7
    """   
    info = mp.get(catalog["movie_status"],"Released")
    rta = [["Año","Total","Promedio votación promedio","Tiempo promedio duración","Ganancia acumulada","Mejor","Peor"]]
    
    if info != None:
        if isinstance(info,list):
            
            for j in range(year_i,year_f+1):
                lista=[]
                total = 0
                vot = 0
                tiempo = 0
                ganancias = 0
                mejor = 0
                peor = 1000000
                for i in range(0,len(info)):
                    fecha = datetime.strptime(info[i]["release_date"], "%Y-%m-%d")
                    fecha = fecha.year
                    lista = info[i]["production_companies"]
                    nombres = []
                    
                    if lista == "Indefinido":
                        nombres.append("Indefinido")
                    else:
                        for elemento in lista:
                            nombres.append(elemento['name'])
                   
                    if (j == fecha) and (str(productora) in str(nombres)):
                        total += 1
                        vot += float(info[i]["vote_average"])
                        tiempo += float(info[i]["runtime"])
                        ganancias += float(info[i]["runtime"] )
                        
                        if mejor<= float(info[i]["vote_average"]):
                            mejor = float(info[i]["vote_average"])
                            nombre_m = info[i]["title"]
                        
                        if peor >= float(info[i]["vote_average"]):
                            peor = float(info[i]["vote_average"])
                            nombre_p = info[i]["title"]
                            
                if total != 0:
                    
                    vot_prom = round(vot/total,2)  
                    tiempo_prom =  round(tiempo/total,2)  
                    mejor_peli = {nombre_m:mejor}
                    peor_peli = {nombre_p:peor}
                    lista = [j, total, vot_prom, tiempo_prom, ganancias, mejor_peli, peor_peli]
                    rta.append(lista)  
       
    return rta
        
def req_8(catalog, year_i, genero):
    """
    Retorna el resultado del requerimiento 8
    """
    """
    Retorna el resultado del requerimiento 7
    """   
    info = mp.get(catalog["movie_status"],"Released")
    rta = [["Año","Total","Promedio votación promedio","Tiempo promedio duración","Ganancia acumulada","Mejor","Peor"]]
    
    if info != None:
        if isinstance(info,list):
            
            for j in range(year_i,2024):
                lista=[]
                total = 0
                vot = 0
                tiempo = 0
                ganancias = 0
                mejor = 0
                peor = 1000000
                for i in range(0,len(info)):
                    fecha = datetime.strptime(info[i]["release_date"], "%Y-%m-%d")
                    fecha = fecha.year
                    lista = info[i]["genres"]
                    nombres = []
                    
                    if lista == "Indefinido":
                        nombres.append("Indefinido")
                    else:
                        for elemento in lista:
                            nombres.append(elemento['name'])
                   
                    if (j == fecha) and (str(genero) in str(nombres)):
                        total += 1
                        vot += float(info[i]["vote_average"])
                        tiempo += float(info[i]["runtime"])
                        ganancias += float(info[i]["runtime"] )
                        
                        if mejor<= float(info[i]["vote_average"]):
                            mejor = float(info[i]["vote_average"])
                            nombre_m = info[i]["title"]
                        
                        if peor >= float(info[i]["vote_average"]):
                            peor = float(info[i]["vote_average"])
                            nombre_p = info[i]["title"]
                            
                if total != 0:
                    
                    vot_prom = round(vot/total,2)  
                    tiempo_prom =  round(tiempo/total,2)  
                    mejor_peli = {nombre_m:mejor}
                    peor_peli = {nombre_p:peor}
                    lista = [j, total, vot_prom, tiempo_prom, ganancias, mejor_peli, peor_peli]
                    rta.append(lista)  
       
    return rta


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
