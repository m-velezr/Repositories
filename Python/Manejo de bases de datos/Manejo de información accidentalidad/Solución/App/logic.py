import time
import os
import csv
from DataStructures.Tree import red_black_tree as bst
from datetime import datetime
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Data/'

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    datos = {"ID":bst.new_map(),
             "Orden" : bst.new_map(),
             "Rango": bst.new_map(),
             "Condados":bst.new_map(),
             "Severidad":bst.new_map(),
             "Latitud":bst.new_map()}
    
    return datos


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    filename = data_dir + filename
   
    input_file = csv.DictReader(open(filename, encoding="utf-8"),
                                delimiter=",")
    num = 1
    for value in input_file:
        ID = int(value["ID"].split('-')[1])
        bst.put(catalog["ID"], ID, value)
        bst.put(catalog['Rango'],value['Visibility(mi)'],value)
        bst.put(catalog['Severidad'],value['Severity'],value)
        bst.put(catalog['Orden'],num,value)
        bst.put(catalog["Condados"],value["County"],value)
        bst.put(catalog["Latitud"],value['Start_Lat'],value)
        num += 1

    
    return num,catalog
        




# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    return bst.get(catalog["ID"],id)


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog,rango,estados):
    """
    Retorna el resultado del requerimiento 2
    """
    # Camilo
    size = 0
    rta = {}
    for est in estados:
        rta[est] = {'Accidentes':0,'Promedio_v':0,'Promedio_d':0,'Mayor':None,'grande':0,'sv':0,'sd':0,"distancia":0 }
    x = bst.values(catalog['Rango'],rango[0],rango[1])
    x = x["elements"]
    if isinstance(x, list):
        for lis in x:
            if not isinstance(lis, list):
                lis = [lis]
                
            for llave in lis:
               
                
                if llave['Severity'] != '':
                    if llave['Severity'] == "4":
                        if llave['State'] in estados:
                            size += 1
                            rta[llave['State']]['Accidentes'] += 1
                            if llave['Visibility(mi)'] != '':
                                rta[llave['State']]['sv'] += float(llave['Visibility(mi)'])
                                rta[llave['State']]['sd'] += float(llave['Distance(mi)'])
                                if float(llave['Visibility(mi)']) > rta[llave['State']]['grande']:
                                    rta[llave['State']]['grande'] = float(llave['Visibility(mi)'])
                                    rta[llave['State']]['Mayor'] = llave["ID"]
                                    rta[llave['State']]['distancia'] = float(llave["Distance(mi)"])
                                
    else:
        if llave['Severity'] == "4":
            if llave['State'] in estados:
                size += 1
                rta[llave['State']]['Accidentes'] += 1
                rta[llave['State']]['sv'] +=float( llave['Visibility(mi)'])
                rta[llave['State']]['sd'] += float(llave['Distance(mi)'])
                if llave['Visibility(mi)'] > rta[llave['State']]['grande']:
                    rta[llave['State']]['grande'] = llave['Visibility(mi)']
                    rta[llave['State']]['Mayor'] = llave["ID"]
                    rta[llave['State']]['Mayor'] = llave
                    
    for esta in estados:
        if esta in rta.keys() and rta[esta]['Accidentes'] != 0:
            rta[esta]['Promedio_v'] = rta[esta]['sv']/ rta[esta]['Accidentes']
            rta[esta]['Promedio_d'] = rta[esta]['sd']/ rta[esta]['Accidentes']
   
    return size, rta

def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog,fecha_i,fecha_f):
    """
    Retorna el resultado del requerimiento 4
    """
    # Mariana
    
    lista = []
    fecha_i = datetime.strptime(fecha_i, '%Y-%m-%d %H:%M:%S')
    fecha_f = datetime.strptime(fecha_f, '%Y-%m-%d %H:%M:%S')
    
    valor_3 = bst.get(catalog["Severidad"],"3")
    valor_4 = bst.get(catalog["Severidad"],"4")
    valores = [valor_3,valor_4]
    
    arr = []
    tot = []
    for i in range(0,len(valores)):
        cant = 0
       
        if  isinstance(valores[i],list):
            lis = valores [i]
            for j in lis:

                inicio = datetime.strptime(j["Start_Time"], '%Y-%m-%d %H:%M:%S')
                fin = datetime.strptime(j["End_Time"], '%Y-%m-%d %H:%M:%S')
                if inicio >= fecha_i and fin<= fecha_f and (j["Visibility(mi)"] != " " and j["Visibility(mi)"] != "")  :
                    if float(j["Visibility(mi)"])<1.0:
                        
                        v = {"Nombre": j["Street"],
                             "Ciudad": j["City"],
                             "Condado": j["County"],
                             "Estado": j["State"],
                             "Severidad" : None,
                             "Visibilidad" : j["Visibility(mi)"],
                             "Prom_Visi": None
                             }
                        
                        
                        cant += 1
                        visi = 0
                        conteo = 0
                        sev = 0

                        for l in lista:
                            if j["Street"] == l["Nombre"] and j["County"] == l["Condado"] and j["State"] == l["Estado"] and j["City"] == l["Ciudad"]:
                                visi += float(l["Visibilidad"])
                                sev += int(l["Severidad"])
                                conteo += 1
                               
                        
                       
                        visi += float(j["Visibility(mi)"])
                        sev += int(j["Severity"])
                        conteo += 1
                        lista.append(v)
                       
                        
                            
                        
                        if len(arr)!= 0:
                            rta = True
                            for f in arr:
                                if f["Nombre"] == j["Street"] and j["County"] == f["Condado"] and j["State"] == f["Estado"] and j["City"] == f["Ciudad"] :
                                    f["Visi"] += visi
                                    f["Cont"] += conteo
                                    f["Severity"] += sev
                                    
                                    rta = False
                            
                            if rta:
                                nodo = {"Nombre": j["Street"],
                                        "Visi": visi,
                                        "Cont":conteo,
                                        "Severity" :sev,
                                        "Condado": j["County"] ,
                                        "Estado":j["State"] ,
                                        "Ciudad":j["City"] }  
                                arr.append(nodo)           
                            
                        else:
                            
                            nodo = {"Nombre": j["Street"],
                             "Visi": visi,
                             "Cont":conteo,
                             "Severity" :sev,
                              "Condado": j["County"] ,
                                "Estado":j["State"] ,
                                "Ciudad":j["City"] }  
                            arr.append(nodo)
                            
        else:
            cant = 1
            lis = valores [i]
            inicio = datetime.strptime(lis["Start_Time"], '%Y-%m-%d %H:%M:%S')
            fin = datetime.strptime(lis["End_Time"], '%Y-%m-%d %H:%M:%S')
            
            if inicio >= fecha_i and fin<= fecha_f and (j["Visibility(mi)"] != " " and j["Visibility(mi)"] != "")  :
                if float(j["Visibility(mi)"])<1.0:
                    lista.append(j)
        
        tot.append(cant)  


    for dicc in arr:
        for via in lista:
            if dicc["Nombre"] == via["Nombre"] and via["Condado"] == dicc["Condado"] and dicc["Estado"] == via["Estado"] and dicc["Ciudad"] == via["Ciudad"]:
                via["Prom_Visi"] = float(dicc["Visi"])/dicc["Cont"]
                via["Severidad"] =  float(dicc["Severity"])/dicc["Cont"]
        
        
    return lista,tot
            
            
                        
            
    
    
     


def req_5(catalog,fecha_i,fecha_f,clima):
    """
    Retorna el resultado del requerimiento 5
    """
    # Camilo
    zonas = ['Mañana','Tarde','Noche','Madrugada']
    t= ['06:00-11:59','12:00-17:59','18:00-23:59','00:00-05:59']
    h = 0
    rta={}
    c ={}
    for climas in clima:
        c[climas] = 0
    for zona in zonas:
        x = c
        rta[zona] = {'Zona':t[h],'Numero':0,'Promedio':0,'Mayor Condicion':None,'ss':0,'Climas':x}
        h += 1
    casos = bst.value_set(catalog['ID'])
    for caso in casos['elements']:
        if caso['Weather_Condition'] in clima:
            i = caso['Start_Time'][0:10]
            f = caso['End_Time'][0:10]
            if (i >= fecha_i) and (fecha_f <=f):
                if 3<=int(caso['Severity']) <=4:
                    t1 = caso['Start_Time'][11:16]
                    t2= caso['End_Time'][11:16]
                    if t1 >= '00:00' and t2 < '06:00':
                        rta['Madrugada']['Numero'] += 1
                        rta['Madrugada']['ss'] += float(caso['Severity'])
                        rta['Madrugada']['Climas'][caso['Weather_Condition']] += 1
                    elif t1 >= '06:00' and t2 < '12:00':
                        rta['Mañana']['Numero'] += 1
                        rta['Mañana']['ss'] += float(caso['Severity'])
                        rta['Mañana']['Climas'][caso['Weather_Condition']] += 1
                    elif t1 >= '12:00' and t2 < '18:00':
                        rta['Tarde']['Numero'] += 1
                        rta['Tarde']['ss'] += float(caso['Severity'])
                        rta['Tarde']['Climas'][caso['Weather_Condition']] += 1
                    elif t1 >= '18:00' and t2 < '24:00':
                        rta['Noche']['Numero'] += 1
                        rta['Noche']['ss'] += float(caso['Severity'])
                        rta['Noche']['Climas'][caso['Weather_Condition']] += 1
                    
    for z in zonas:
        if rta[z]['Numero'] != 0:
            rta[z]['Promedio'] = rta[z]['ss'] /rta[z]['Numero'] 
            m = 0
            for a,b in rta[z]['Climas'].items():
                if b > m :
                    rta[z]['Mayor Condicion'] = a
                    m = int(b)
    return rta


def req_6(catalog,fecha_i,fecha_f,condados,umbral_H, umbral_T):
    """
    Retorna el resultado del requerimiento 6
    """
    # Mariana
    lista_prom = []
    grave = []
    final = []
    
    fecha_i = datetime.strptime(fecha_i, '%Y-%m-%d %H:%M:%S')
    fecha_f = datetime.strptime(fecha_f, '%Y-%m-%d %H:%M:%S')
    for nom in condados:
        temp=cant = hum=vel=dist= 0
        mayor = 0
        date_i = temperatura= ID_ma = humedad = distancia = descripcion = None
        lista = {nom : []}
        
        lis = bst.get(catalog["Condados"],nom)
        if  isinstance(lis,list):
            for j in lis:
                inicio = datetime.strptime(j["Start_Time"], '%Y-%m-%d %H:%M:%S')
                fin = datetime.strptime(j["End_Time"], '%Y-%m-%d %H:%M:%S')
                if inicio >= fecha_i and fin<= fecha_f and j["Humidity(%)"] != '' and j["Temperature(F)"] != '' and j["Severity"] != '':
                    
                    if float(j["Humidity(%)"])<=float(umbral_H) and float(j["Temperature(F)"])<=float(umbral_T) and (int(j["Severity"])==3 or int(j["Severity"])==4):
                        rta = True
                        cant += 1
                        temp += float(j["Temperature(F)"])
                        hum += float(j["Humidity(%)"])
                        if j["Wind_Speed(mph)"] != '':
                            vel += float(j["Wind_Speed(mph)"]) 
                    
                        dist += float(j["Distance(mi)"])
                        
                        if int(j["Severity"]) >= mayor:
                            mayor = int(j["Severity"])
                            ID_ma = j["ID"]
                            date_i = inicio
                            temperatura = float(j["Temperature(F)"])
                            humedad = float(j["Humidity(%)"])
                            distancia = float(j["Distance(mi)"])
                            descripcion = j["Description"]
                        
                        y = {   "Condado": nom,
                                 "ID": ID_ma,
                                "Fecha Inicio": inicio,
                                "Temperatura(F)": temperatura,
                                "Humedad(%)": humedad,
                                "Distancia Afectada": distancia,
                                "Descripción del accidente": descripcion
                                }
                        
                        lista[nom].append(y)
            final.append(lista)      
                        
        else:
            
            
            inicio = datetime.strptime(lis["Start_Time"], '%Y-%m-%d %H:%M:%S')
            fin = datetime.strptime(lis["End_Time"], '%Y-%m-%d %H:%M:%S')
            
            if inicio >= fecha_i and fin<= fecha_f and j["Humidity(%)"] != '' and j["Temperature(F)"] != '' and j["Severity"] != '':
                if float(lis["Humidity(%)"])<=umbral_H and float(lis["Temperature(F)"])<=umbral_T and (int(j["Severity"])==3 or int(j["Severity"])==4):
                    cant = 1
                    temp = float(j["Temperature(F)"])
                    hum = float(j["Humidity(%)"])
                    if j["Wind_Speed(mph)"] != '':
                            vel = float(j["Wind_Speed(mph)"]) 
                    
                    dist = float(j["Distance(mi)"])
                    y = {"Condado":nom,
                                "ID": ID_ma,
                                "Fecha Inicio": inicio,
                                "Temperatura(F)": temperatura,
                                "Humedad(%)": humedad,
                                "Distancia Afectada": distancia,
                                "Descripción del accidente": descripcion
                                }
                        
                    lista[nom].append(y)
                    final.append(lista)      
        if rta:                    
            v = {"Condado" : nom,
                "Temperatura Prom": round(temp/cant,2),
                "Humedad Prom":round(hum/cant,2),
                "Velocidad Prom Viento":round(vel/cant,2),
                "Distancia Prom (mi)":round(dist/cant,2),
                "Número de Accidentes": cant}

            lista_prom.append(v)
            rta = False
            
        if mayor != 0:
            x = {"Condado":nom,
                 "ID": ID_ma,
                "Fecha Inicio": inicio,
                "Temperatura(F)": temperatura,
                "Humedad(%)": humedad,
                "Distancia Afectada": distancia,
                "Descripción del accidente": descripcion
                }
            grave.append(x)
   
   
    return lista_prom, grave, final

def req_7(catalog, la_minima, la_maxima,lo_minima, lo_maxima):
    """
    Retorna el resultado del requerimiento 7
    """


    rta ={'size':0, 'elements':[]}
    lista = bst.values(catalog['Latitud'],la_minima,la_maxima)
    lista = lista["elements"]
    for elemento in lista:
        if isinstance(elemento,list):
            for dic in elemento:
                if dic['End_Lat'] != '' and dic['Start_Lng'] != '' and dic['End_Lng'] != '' :
                    
                    if float(dic['End_Lat']) < float(la_maxima) and float(lo_minima) < float(dic['Start_Lng']) and float(dic['End_Lng']) < float( lo_maxima):
                        h1 = datetime.strptime(dic['Start_Time'].split()[1], "%H:%M:%S")
                        h2 = datetime.strptime(dic['End_Time'].split()[1], "%H:%M:%S")
                        if h2 > h1:
                            diferencia = h2 - h1
                        else:
                            diferencia = h1 - h2 
                        minutos = diferencia.total_seconds() / 60
                        a = dic['Description']
                        if len(dic['Description']) > 40:
                            a = dic['Description'][0:41]
                        x =  [dic['ID'],dic['Start_Time'],dic['City'],dic['State'],a,minutos,dic['Start_Lat'],dic['End_Lat'],dic['Start_Lng'],dic['End_Lng']]
                        rta['elements'].append(x)
                        
                        rta['size'] += 1
        elif elemento['End_Lat'] != '' and elemento['Start_Lng'] != '' and elemento['End_Lng'] != '':
            if float(elemento['End_Lat'])< float(la_maxima) and float(lo_minima )< float(elemento['Start_Lng']) and float(elemento['End_Lng']) < float(lo_maxima):
                h1 = datetime.strptime(elemento['Start_Time'].split()[1], "%H:%M:%S")
                h2 = datetime.strptime(elemento['End_Time'].split()[1], "%H:%M:%S")
                if h2 > h1:
                    diferencia = h2 - h1
                else:
                    diferencia = h1 - h2 
                minutos = diferencia.total_seconds() / 60
                a = elemento['Description']
                if len(elemento['Description']) > 40:
                    a = elemento['Description'][0:41]
                x =x =  [elemento['ID'],elemento['Start_Time'],elemento['City'],elemento['State'],a,minutos,elemento['Start_Lat'],elemento['End_Lat'],elemento['Start_Lng'],elemento['End_Lng']]
                rta['elements'].append(x)
                rta['size'] += 1
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
