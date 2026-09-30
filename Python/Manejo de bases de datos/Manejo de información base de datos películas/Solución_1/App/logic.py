import time
from DataStructures import single_linked_list as lt
import csv
csv.field_size_limit(2147483647)
import json
from datetime import datetime

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {"movies": None}
    
    catalog["movies"] = lt.new_list() 
   
    return catalog

# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    ult = None
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
        
        lt.add_last(catalog["movies"],movie)
    size = catalog["movies"]["size"]

    
    return size

# Funciones de consulta sobre el catálogo
def elements(catalog):
    list_prim = []
    list_ult = []
    dicc = {"Fecha publicación": None,
            "Título": None,
            "Idioma original": None,
            "Duración en min" : None,
            "Presupuesto de producción": None,
            "Ingresos de taquilla netos": None,
            "Ganacias de la película": None
            }
    rta = True
    actual = catalog["movies"]["first"]
    
    for i in range(0,5):
        dicc["Fecha publicación"] = actual["info"]["release_date"]
        dicc["Título"] = actual["info"]["title"]
        dicc["Idioma original"] = actual["info"]["original_language"]
        dicc["Duración en min"] = actual["info"]["runtime"]
        dicc["Presupuesto de producción"]= actual["info"]["budget"]
        dicc["Ingresos de taquilla netos"] = actual["info"]["revenue"]
        dicc["Ganancias de la película"] = actual["info"]["ganancias"]
        
        list_prim.append(dicc.copy())
        actual = actual["next"]
    
    while rta :
        if actual["next"]["next"]["next"]["next"]["next"]== None:
            for i in range(0,5):
                dicc["Fecha publicación"] = actual["info"]["release_date"]
                dicc["Título"] = actual["info"]["title"]
                dicc["Idioma original"] = actual["info"]["original_language"]
                dicc["Duración en min"] = actual["info"]["runtime"]
                dicc["Presupuesto de producción"]= actual["info"]["budget"]
                dicc["Ingresos de taquilla netos"] = actual["info"]["revenue"]
                dicc["Ganancias de la película"] = actual["info"]["ganancias"]
                
                list_ult.append(dicc.copy())
                actual = actual["next"]
            rta = False
        else:
            actual = actual["next"]
    return list_prim, list_ult

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    pos=  lt.is_present(catalog['movies'], id, compare_ids)
    if pos >= 0:
        movie = lt.get_element(catalog['movies'], pos)
        return movie
    return None

def compare_ids(id, movie):
    if id == movie["id"]:
        return 0
    elif id > movie["id"]:
        return 1
    else:
        return -1

def req_1(catalog, time):
    """
    Retorna el resultado del requerimiento 1
    """
    actual = catalog["movies"]["first"]
    fecha_ant = datetime(1500,1,1)
    peli = ""
    contador = 0
    for i in range(catalog["movies"]["size"]):
        
        if float(actual["info"]["runtime"]) >= float(time):
            fecha = datetime.strptime(actual["info"]["release_date"], "%Y-%m-%d")
            contador += 1
            if fecha > fecha_ant :
                fecha_ant = fecha
                peli = actual["info"]
            actual = actual["next"]
        else:
            actual = actual["next"]
            
    return peli, contador
    

def req_2(catalog, idioma):
    """
    Retorna el resultado del requerimiento 2
    """
    """
    actual = catalog["movies"]["first"]
    fecha_ant = datetime(1500,1,1)
    peli = ""
    contador = 0
    for i in range(catalog["movies"]["size"]):
        
        if actual["info"]["original_language"] == idioma:
            fecha = datetime.strptime(actual["info"]["release_date"], "%Y-%m-%d")
            contador += 1
            if fecha > fecha_ant :
                fecha_ant = fecha
                peli = actual["info"]
            actual = actual["next"]
        else:
            actual = actual["next"]
            
    return peli, contador
    """
    pass


def req_3(catalog,idioma,fecha_inicial,fecha_final):
    """
    Retorna el resultado del requerimiento 3
    """
    rta ={'Numero_peliculas':0,
          'Tiempo_promedio':0,
          'peliculas': []}
    t = 0
    nodo = catalog['movies']['first']
    for i in range(catalog['movies']['size']):
        gana = float(nodo['info']['revenue'])-float(nodo['info']['budget'])
        if fecha_inicial <= nodo['info']['release_date'] <= fecha_final:
            peli = {'fecha_publicacion': nodo['info']['release_date'],
                'Titulo':nodo['info']['title'],
                'Presupuesto':float(nodo['info']['budget']),
                'Recaudo':float(nodo['info']['revenue']),
                'Ganania':gana,
                'Duracion':float(nodo['info']['runtime']),
                'Puntaje':float(nodo['info']['vote_average']),
                'Estado':nodo['info']['status'],}
            rta['Numero_peliculas'] += 1
            rta['peliculas'].append(peli)
            t += float(nodo['info']['runtime'])
        nodo = nodo['next']
    if rta['Numero_peliculas'] > 0:
        rta['Tiempo_promedio'] = t / rta['Numero_peliculas']
    else:
        rta['Tiempo_promedio'] = 0  
    return rta
def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog, fech_inf, fech_sup, t_inf, t_sup):
    """
    Retorna el resultado del requerimiento 5
    """
    actual = catalog["movies"]["first"]
    peli = []
    contador = 0
    duracion = 0
    fech_inf = datetime.strptime(fech_inf, "%Y-%m-%d")
    fech_sup = datetime.strptime(fech_sup, "%Y-%m-%d")
    
    dicc = {"Fecha publicación": None,
            "Título": None,
            "Idioma original": None,
            "Duración en min" : None,
            "Presupuesto de producción": None,
            "Ingresos de taquilla netos": None,
            "Ganacias de la película": None
            }
    for i in range(catalog["movies"]["size"]):
        
        if float(actual["info"]["runtime"]) >= float(t_inf) and float(actual["info"]["runtime"]) <= float(t_sup)  :
            fecha = datetime.strptime(actual["info"]["release_date"], "%Y-%m-%d")
            if fecha >= fech_inf and fecha <= fech_sup:
                duracion += float(actual["info"]["runtime"])
                contador += 1
                
                dicc["Fecha publicación"] = actual["info"]["release_date"]
                dicc["Título"] = actual["info"]["title"]
                dicc["Idioma original"] = actual["info"]["original_language"]
                dicc["Duración en min"] = actual["info"]["runtime"]
                dicc["Presupuesto de producción"]= actual["info"]["budget"]
                dicc["Ingresos de taquilla netos"] = actual["info"]["revenue"]
                dicc["Ganancias de la película"] = actual["info"]["ganancias"]
                dicc["Puntaje de calificación de la película"] = actual["info"]["vote_average"]
                
                peli.append(dicc.copy())
                
                actual = actual["next"]
        
            else:
                actual = actual["next"]
        else:
            actual = actual["next"]
    
    if  contador == 0:
        prom = "No hay"   
    else:
        prom = duracion/contador
 
    return peli, contador, prom
def req_6(catalog,idioma, anio_inicial,anio_final):
    """
    Retorna el resultado del requerimiento 6
    """
    rta = []
    f1 = int(anio_inicial)
    f2 = int(anio_final)
    anio = int(anio_inicial)
    for j in range(f2-f1+1):
        
        nodo = catalog['movies']['first']
        cantidad = vota = tiempo = ganan = mv = 0
        pv = 100
        for i in range(catalog['movies']['size']):
            a = int(nodo['info']['release_date'][0:4])
            if (nodo['info']['status'] == 'Released')and(a==anio)and(idioma == nodo['info']['original_language']):
                cantidad += 1
                vota += float(nodo['info']['vote_average'])
                tiempo += float(nodo['info']['runtime'])
                ganan += float(nodo['info']['revenue'])-float(nodo['info']['budget'])
                if float(nodo['info']['vote_average']) <= pv:
                    peor = nodo['info']
                    pv = float(nodo['info']['vote_average'])
                if float(nodo['info']['vote_average']) >= mv:
                    mejor = nodo['info']
                    mv = float(nodo['info']['vote_average'])
            nodo = nodo['next']
        if cantidad != 0: 
            este = {'anio': anio,
                    'numero_peliculas':cantidad,
                    'promedio_votacion': vota/cantidad ,
                    'tiempo_promedio' : tiempo/cantidad ,
                    'ganancias': ganan,
                    'mejor_promedio': mejor,
                    'peor_promedio':peor  }               
            rta.append(este)
        anio += 1

    return rta



def req_7(catalog,productora, anio_inicial,anio_final):
    """
    Retorna el resultado del requerimiento 7
    """
    rta = []
    f1 = int(anio_inicial)
    f2 = int(anio_final)
    anio = int(anio_inicial)-1
    for j in range(f2-f1+2):
        anio += 1
        nodo = catalog['movies']['first']
        cantidad = vota = tiempo = ganan = mv = 0
        pv = 100
        for i in range(catalog["movies"]['size']):
            a = int(nodo['info']['release_date'][0:4])
            produ = nodo['info']['production_companies']
            x = ''
            if produ != "Indefinido":
                for dicc in produ:
                    x += dicc["name"]
            if (nodo['info']['status'] == 'Released')and((a)==anio)and(productora in x):
                print(nodo['info']['status'],(a),x,productora)
                cantidad += 1
                vota += float(nodo['info']['vote_average'])
                tiempo += float(nodo['info']['runtime'])
                ganan += float(nodo['info']['revenue'])-float(nodo['info']['budget'])
                if float(nodo['info']['vote_average']) <= pv:
                    peor = nodo['info']
                    pv = float(nodo['info']['vote_average'])
                if float(nodo['info']['vote_average']) >= mv:
                    mejor = nodo['info']
                    mv = float(nodo['info']['vote_average'])
            nodo = nodo['next']
        
        if cantidad != 0: 
            este = {'anio': anio,
                    'numero_peliculas':cantidad,
                    'promedio_votacion': vota/cantidad ,
                    'tiempo_promedio' : tiempo/cantidad ,
                    'ganancias': ganan,
                    'mejor_promedio': mejor,
                    'peor_promedio':peor                 
                        }

            rta.append(este)
        
    return rta


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


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
