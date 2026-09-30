from.import list_node as node
def new_list():
    new_list = {'first': None,
                'last': None,
                'size': 0}
    return new_list

def add_first(my_list, element):
    nod = node.new_single_node(element)
    
    if my_list['first'] is None:
        my_list['first'] = nod
        my_list['last'] = nod
        my_list['size'] += 1
    else:
        nod['next'] = my_list['first']
        my_list['first'] = nod
        my_list['size'] += 1
    return my_list

def add_last(my_list, element):
    nod = node.new_single_node(element)
    if my_list['first']== None:
        my_list['first'] = nod
        my_list['last'] = nod
        
    else:
        actual = my_list['first']
        while actual['next'] is not None:
            actual = actual['next']
        actual['next'] = nod
        my_list['last'] = nod
    
    my_list['size'] += 1
    
    return my_list

def size(my_list):
    return my_list['size']

def first_element(my_list):
    return my_list['first']['info']

def is_empty(my_list):
    rta = False
    if my_list["size"] == 0:
        rta = True
    return rta 

def get_element(my_list, pos):
    if pos >= 0 and pos < my_list["size"]:
        if pos == 0:
            actual = my_list["first"]["info"]
            valor = actual
        else:
            
            actual = my_list["first"]["next"]
            veces = 1
            while veces <= pos :
                valor = actual["info"]
                actual = actual["next"]
                veces += 1
    return valor

def last_element(my_list):
    if my_list["size"] != 0 :
        return my_list["last"]["info"]
        
def remove_first(my_list):
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1
    return my_list["first"]["info"]

def remove_last(my_list):
    if my_list["size"] == 0:
        return None
    elif my_list["size"] == 1:
        rta = my_list['first']
        my_list["first"] = None
        my_list["last"] = None
    else:
        rta = my_list['last']
        actual = my_list["first"]
        while actual["next"]["next"] is not None:
            actual = actual["next"]
        actual["next"] = None
        my_list["last"] = actual
    
    my_list["size"] -= 1
    
    
    return rta['info']

def insert_element(my_list, element, pos):
    nodo = node.new_single_node(element)
    if pos == 0:
        nodo["next"] = my_list["first"]
        my_list["first"] = nodo
        if my_list["size"] == 0:
            my_list["last"] = nodo
    else:
        i = 0
        actual = my_list["first"]
        while i < pos - 1 and actual is not None:
            actual = actual["next"]
            i += 1
        
        if actual is not None:
            nodo["next"] = actual["next"]
            actual["next"] = nodo
            
            if nodo["next"] is None:  
                my_list["last"] = nodo
       
    
    my_list["size"] += 1
    return my_list
    
def is_present(my_list, element, cmp_function):
    
    valor = -1
    if my_list["size"] != 0 :
        i = 0
        actual = my_list["first"]
        while i < my_list["size"]:
            if cmp_function(element, actual["info"]) == 0:
                valor = i
                break
            else:
                actual = actual["next"]
                i += 1
    return valor    
    
def change_info(my_list, pos, new_info):
    
    if my_list["size"] != 0 :
        i = 0
        actual = my_list["first"]
        while i < my_list["size"]:
            if pos == i:
                actual["info"] = new_info
                break
            else:
                actual = actual["next"]
                i += 1
    return my_list            


def exchange(my_list, pos1, pos2):
    if (pos1 >= 0 and pos2 >= 0) and (pos1<my_list["size"] and pos2<my_list["size"]):
        
        
        actual1 = my_list["first"]
        actual2 = my_list["first"]
        valor_1 = None
        valor_2 = None
    
        
        for i in range(0, pos1):
            actual1 = actual1["next"]
        valor_1 = actual1["info"]
        
        for j in range(0, pos2):
            actual2 = actual2["next"]
        valor_2 = actual2["info"]

        actual1["info"] = valor_2
        actual2["info"]= valor_1
                
    return my_list
            
def sub_list(my_list, pos, num_elem):
    
    if pos >= 0 and pos < my_list["size"] and num_elem <= my_list["size"]-pos:
        actual = my_list["first"]
        lista = {"first" : None,
                 "last" : None,
                 'size': 0}
        c = 0
        for i in range(0, my_list["size"]):
            if i>=pos-1  and c <= my_list['size']-num_elem:
                nodo = {"info": actual["info"], "next" : actual["next"]}
                if pos == i:
                    lista["first"] = nodo
                elif num_elem == i+1:
                    lista["last"] = nodo    
               
                
                lista["size"] += 1
                c += 1
            actual = actual["next"]
    return lista
                
                

def delete_element (my_list,pos):
    if pos == 0:
        my_list['first'] = my_list['first']['next']
        my_list['size'] -= 1
    else:
        l = my_list['first']    
        for i in range(0, my_list['size']):
            if i == pos:
                a['next'] = l['next']
                my_list['size'] -= 1
                if i == my_list['size']:
                    my_list['last'] = a
            a = l
            l = a['next']
    return my_list


            
            
        
        
    
            

    