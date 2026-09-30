import random
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as lt

def new_map(num_elements, load_factor, prime=109345121):
    
    tabla = {"prime": prime,
             "capacity": mf.next_prime(num_elements/load_factor),
             "scale": random.randint(1, prime-1),
             "shift": random.randint(1, prime-1),
             "table":[None]*mf.next_prime(num_elements/load_factor) ,
             "current_factor": 0,
             "limit_factor": load_factor,
             "size": 0,
             "type": "PROBING"
    }
    return tabla

def put(my_map,key,value):
    if my_map["size"] > my_map["capacity"]*my_map["limit_factor"]:
        my_map = rehash(my_map)
    poner = {key:value}
    pos = (((my_map['scale']*hash(key))+my_map['shift'])% my_map['prime'])%my_map['capacity']
    if my_map['table'][pos] == None or my_map['table'][pos] == '__EMPTY__':
        my_map['table'][pos] = [poner]
        my_map['size'] += 1
    
    else:
       
        puesto = False
        for dic in my_map['table'][pos]:
            if key in dic.keys():
                if not isinstance(dic[key], list):
                    info = [dic[key]]
                    info.append(value)
                    dic[key] = info
                    
                else:
                    dic[key].append(value)
                
                puesto = True
        if not puesto:
            my_map['table'][pos].append(poner)
            my_map['size'] += 1
    return my_map

def contains(my_map, key):
    rta = False
    for lista in my_map['table']:
        if lista != None and lista != '__EMPTY__':
            for dic in lista:
                if dic != '__EMPTY__' and key in dic.keys():
                    rta = True
    return rta


    
def get(my_map, key):
    rta = None
    pos = (((my_map['scale']*hash(key))+my_map['shift'])% my_map['prime'])%my_map['capacity']
    if my_map['size'] > 0 and my_map['table'][pos] != None :
        for dic in my_map['table'][pos]:
            if dic != None and dic != '__EMPTY__':
                if key in dic.keys():
                    rta = dic[key]
    return rta


def remove(my_map, key):
    pos = (((my_map['scale']*hash(key))+my_map['shift'])% my_map['prime'])%my_map['capacity']
    if my_map["size"] != 0 and my_map['table'][pos] != None:
        p_lista = 0
        for dic in my_map['table'][pos]:
            if dic != '__EMPTY__' :
                if key in dic.keys():
                    my_map['table'][pos][p_lista] = '__EMPTY__'
                    my_map['size'] -= 1
            p_lista += 1
    return my_map
        


def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    if my_map["size"] == 0:
        return True
    else:
        return False
    
def key_set(my_map):
    l = lt.new_list()
    if my_map["size"] != 0:
        for lista in my_map["table"]:
            if lista is not None :
                for dicc in lista:
                    if dicc != '__EMPTY__':
                        l["elements"].append(list(dicc.keys())[0])
                        l["size"]+= 1
    return l

def value_set(my_map):
    l = lt.new_list()
    if my_map["size"] != 0:
        for lista in my_map["table"]:
            if lista is not None :
                for dicc in lista:
                    if dicc != '__EMPTY__':
                        l["elements"].append(list(dicc.values())[0])
                        l["size"]+= 1
    return l

def find_slot(my_map, key, hash_value):
    if my_map['table'][hash_value] == None:
        return False, hash_value
    else:
        encontrada = False
        for dic in my_map['table'][hash_value]:
            if key in dic.keys():
                encontrada = True
                return True,hash_value
        if encontrada == False:
            p = 0 
            for i in my_map['table']:
                if (i == None or i[0] == '__EMPTY__') and p>= hash_value:
                    return False, p
                p +=1
                
                
def is_available(table, pos):
    if table[pos] == None or table[pos][0]=='__EMPTY__':
        return True
    else:
        return False

def rehash(my_map):
    n_map = my_map
    n_map['capacity'] *= 2
    
    return my_map


def default_compare(key, element):
    if key == element:
        return 0
    if key > element:
        return 1
    else:
        return -1
    
def rehash(my_map):
    # Nueva capacidad como el doble de la original más 1
    nueva_capacidad = my_map["size"] * 2 + 1
    
    # Crear un nuevo mapa con la nueva capacidad
    nuevo_mapa = new_map(nueva_capacidad, my_map["limit_factor"])
    
    # Transferir elementos de la tabla original al nuevo mapa
    for bucket in my_map["table"]:
        if bucket is not None:
            for dicc in bucket:
                if dicc != '__EMPTY__':
                    # Inserta la clave y el valor en el nuevo mapa
                    for clave, valor in dicc.items():
                        put(nuevo_mapa, clave, valor)
    
    return nuevo_mapa

    