import time
import os
import csv
from DataStructures.Graph import adj_list_graph as graph
from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as lt
import datetime
import sys

# Establece una nueva profundidad máxima de recursión
sys.setrecursionlimit(8000)

# Imprime la profundidad actual de recursión
print(sys.getrecursionlimit())


data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Data/'

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {"Relaciones": graph.new_graph(),
               "Usuarios": mp.new_map(300000,0.8),
               "seguidores":None}
    
    
    return catalog

# Funciones para la carga de datos

def load_data(catalog, relationship, users):
    """
    Carga los datos del reto
    """
    rela = data_dir + relationship
    usu = data_dir + users
   
    rela_file = csv.DictReader(open(rela, encoding="latin-1"),
                                delimiter=";")
    
    usu_file = csv.DictReader(open(usu, encoding="latin-1"),
                                delimiter=";")
    x = {}
    dic_conexiones = {}
    for lin1 in rela_file:
        graph.insert_vertex(catalog["Relaciones"],lin1["FOLLOWED_ID"],lin1["FOLLOWER_ID"],lin1["START_DATE"])
        if lin1["FOLLOWED_ID"] not in dic_conexiones:
            dic_conexiones[lin1["FOLLOWED_ID"]] = 1
            x[lin1['FOLLOWED_ID']] = 1
        elif lin1["FOLLOWED_ID"]  in dic_conexiones:
            dic_conexiones[lin1["FOLLOWED_ID"]] += 1
            x[lin1['FOLLOWED_ID']] +=1
    catalog['seguidores'] = x
   
    basic = 0
    premium = 0 
    
    dic_ciudad = {}
    
    for lin2 in usu_file:
        mp.put(catalog["Usuarios"], str(int(float(lin2["USER_ID"]))),lin2)    
        if lin2["USER_TYPE"]=="basic":
            basic += 1
        else:
            premium += 1
        
        if lin2["CITY"] not in dic_ciudad:
            dic_ciudad[lin2["CITY"]] = 1
        elif lin2["CITY"]  in dic_ciudad:
            dic_ciudad[lin2["CITY"]] += 1
   
    
    tot_usu = mp.size(catalog["Usuarios"])
    conexiones = graph.edges(catalog["Relaciones"])
    tot_basic = basic
    tot_premium = premium
    
    for val in dic_conexiones:
        dic_conexiones[val] = round(dic_conexiones[val]/conexiones,5)
    
    mayor = 0
    for val2 in dic_ciudad:
        if  dic_ciudad[val2] > mayor:
            mayor = dic_ciudad[val2]
            ciu = val2

    return tot_usu, conexiones, tot_basic, tot_premium, dic_conexiones, [ciu,mayor]  
    

        
        
        
# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def depth_first_search(my_graph, source):
    vertices = graph.vertices(my_graph)
    search = {'source':source, 'visited':None}
    search['visited'] = mp.new_map(vertices['size'],load_factor=0.5)
    mp.put(search['visited'],source,{'marked':True,'edge_to':None})
    dfs_vertex(search,my_graph,source)
    return search
def sacar_mapa(mapa,source):
    vert = mapa['table']
    rta = []
    for v in vert:
        if v != None:
            x = v[0]
            if str(source) == list(x.keys())[0]:
                if isinstance(x,list):
                    for ele in x:
                        rta.append(ele)
                else:
                    rta.append(x)
    return rta                
    
def dfs_vertex(search, graph, source):
    info = sacar_mapa(graph['vertices'], source)
    if info == None or not isinstance(info, list):
        return None  
    
    for dic in info:
        dic = dic[source]
        if isinstance(dic,list):
            dic = dic[0]
        vertex_b = dic['vertex_b']
        if vertex_b != None:
            v = mp.get(search['visited'], vertex_b)
            if v == None or not v.get('marked', False):
                mp.put(search['visited'], vertex_b, {'marked': True, 'edge_to': source})
                dfs_vertex(search, graph, vertex_b)

    return None



def has_path_to(search, vertex):
    if vertex == search['source']:
        return True
    pos = (((search['visited']['scale'] * hash(vertex)) + search['visited']['shift']) % search['visited']['prime']) % search['visited']['capacity']
    v = search['visited']['table'][pos]
    if v is None:
        return False
    d = None
    for dic in v:
        if vertex in dic:
            d = dic
            break
    if d is None:
        return False
    if 'edge_to' in d[vertex]:
        edge_to = d[vertex]['edge_to']
        if edge_to is not None:
            return has_path_to(search, edge_to)
    return False

def req_1(catalog, vertex1, vertex2):
    """
    Retorna el resultado del requerimiento 1
    """
    tabla = depth_first_search(catalog['Relaciones'],vertex1)
    rta = has_path_to(tabla,vertex2)
    info = mp.get(catalog['Usuarios'],vertex1)
    info2 = mp.get(catalog['Usuarios'],vertex2)
    mandar1 = None
    mandar2 = None
    if rta:
        mandar1 = info[['USER_ID'],info['USER_NAME'],info['USER_TYPE']]
        mandar2 = [info2['USER_ID'],info2['USER_NAME'],info2['USER_TYPE']]
    return rta,mandar1,mandar2

def buscar(graph,v,vertex2, pasos, lenght):
    pass
    
    n = 0

def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog,ID):
    """
    Retorna el resultado del requerimiento 3
    """
    lista_seguidores = mp.get(catalog["Relaciones"]["vertices"],ID)
    seg = []
    amigos = []
    for v in lista_seguidores:
        if isinstance(v,list):
            v= v[0]
        seg.append(v["vertex_b"])
    
    for a in seg:
        ami = mp.get(catalog["Relaciones"]["vertices"],a)
        if ami is None:
            amigos.append(0)
        else:
            amigos.append(len(ami))
    
    mayor = 0
    for i in range(0, len(amigos)):
        if amigos[i] > mayor:
            mayor = amigos[i]
            pos = i
    cant = amigos[pos]
    amigo = seg[pos]
    return cant,amigo
            
            
    

def req_4(catalog,ID1,ID2):
    """
    Retorna el resultado del requerimiento 4
    """
    lista_seguidores1 = sacar_mapa(catalog["Relaciones"]["vertices"],ID1)
    lista_seguidores2 = sacar_mapa(catalog["Relaciones"]["vertices"],ID2)
    seg1 = []
    if lista_seguidores1 == None or lista_seguidores2 == None:
        return ['no hay']
    rta=[['Id','Nombre','Tipo U']]
    for vex in lista_seguidores1:
        x = vex[ID1]
        if isinstance(x,list):
            for ele in x:
                if isinstance(ele,list):
                    ele = ele[0]
                seg1.append(ele["vertex_b"])
        if isinstance(x,list):
            x = x[0]
        seg1.append(x["vertex_b"])
    
    for v in lista_seguidores2:
        y = v[ID2]
        if isinstance(v,list):
            for ele in y:
                if isinstance(ele,list):
                    ele = ele[0]
                cosa = ele['vertex_b']
                if cosa in seg1:
                    info = mp.get(catalog['Usuarios'],cosa)
                    x = [info['USER_ID'],info['USER_NAME'],info['USER_TYPE']]
                    rta.append(x)
        if isinstance(y,list):
            y=y[0]
        cosa = y['vertex_b']
        if cosa in seg1:
            info = mp.get(catalog['Usuarios'],cosa)
            x = [info['USER_ID'],info['USER_NAME'],info['USER_TYPE']]
            rta.append(x)
    return rta
def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog,N):
    """
    Retorna el resultado del requerimiento 6
    """
    N = int(N)
    lis_seguidores = catalog['seguidores']
    rta= [['Cuenta','Nombre','Seguidores']]
    mayores = {}
    for cuenta, num in lis_seguidores.items():
        if len(mayores) < N:
            x = mp.get(catalog['Usuarios'],cuenta)
            if x != None:
                mayores[num] = [cuenta,x['USER_NAME']]
        else:
            if num > min(mayores):
                x = mp.get(catalog['Usuarios'],cuenta)
                if x != None:
                    mayores.pop(min(mayores))
                    mayores[num] = [cuenta,x['USER_NAME']]
                    source = cuenta
    conexion = True
    search = depth_first_search(catalog['Relaciones'],source)
    for cantidad, info in mayores.items():
        rta.append([info[0],info[1],cantidad])
        conexion = has_path_to(search,info[0])
    if conexion:
        rta2 = 'El arbol '+str(source)+ ' conecta todos'
    else:
        rta2 = 'No son conectados'
    return rta , rta2
def req_7(catalog,ID,hob):
    """
    Retorna el resultado del requerimiento 7
    """
    
    vert = mp.get(catalog["Relaciones"]["vertices"],ID)
    hob_ex = []
    prof_ex = []
    prof_imp = []
    exp = []
    imp = []
    hob_imp = []
    nivel = 1
    if vert is not None:
        for v in vert:
            if isinstance(v,list):
                v= v[0]
            busc = v["vertex_b"]
            ho = mp.get(catalog["Usuarios"],busc)
            if ho != None:
                lista = eval(ho["HOBBIES"])
                l = []
                rta = False
                for h in hob:
                    for h2 in lista:
                        if h == h2:
                            l.append(h)
                            rta = True
                    
                
                hob_ex.append(l)  
                if rta:
                    exp.append(busc)
                    prof_ex.append(1)           
        
        rec = exp.copy()
        rec.append(ID)
        if len(exp)!= 0:
            imp_1,hob_imp1,prof_imp1=masc_7(catalog,exp,hob,imp,hob_imp,prof_imp,nivel,rec)
            return imp_1,hob_imp1,prof_imp1, exp,hob_ex,prof_ex
            
        else:
            return imp,hob_imp,prof_imp, exp,hob_ex,prof_ex
    else:
        return imp,hob_imp,prof_imp, exp,hob_ex,prof_ex
        
    
def masc_7(catalog,lis,hob,imp,hob_imp,prof_imp,nivel,rec):
    nivel += 1
    
    if nivel == mp.size(catalog["Usuarios"]):
        return imp,hob_imp,prof_imp
    
    
    else:  
        for e in lis:
            verti = mp.get(catalog["Relaciones"]["vertices"],e)
            if verti is not None:
                for v in verti:
                    if isinstance(v,list):
                        v= v[0]
                    busc = v["vertex_b"]
                    for val in rec:
                        rt = True
                        if val == busc:
                            rt = False
                    if rt:    
                        ho = mp.get(catalog["Usuarios"],busc)
                        if ho != None:
                            lista = eval(ho["HOBBIES"])
                            l = []
                            rta = False
                            for h in hob:
                                for h2 in lista:
                                    if h == h2:
                                        l.append(h)
                                        rta = True
                                
                            
                            hob_imp.append(l)  
                            if rta:
                                imp.append(busc)
                                prof_imp.append(nivel)
                                rec.append(busc)         
           
               
        if len(imp)!= 0:
            lis = imp.copy()
            return masc_7(catalog,lis,hob,imp,hob_imp,prof_imp,nivel,rec)
        
        else:
            return imp,hob_imp,prof_imp
    
                                    
                                    
                    
    


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
