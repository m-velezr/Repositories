
from DataStructures.Tree import rbt_node as rbt_node

def new_map():
    tree = {"root": None,
            "type": "RBT"}
    return tree

def put(my_rbt, key, value):
    if my_rbt['root'] == None:
        my_rbt['root'] = rbt_node.new_node(key,value,1)
        return my_rbt
    root = my_rbt['root']
    my_rbt["root"]=insert_node(root, key, value)
    my_rbt['root']['color'] = 1
    return my_rbt

def insert_node(root,key,value):

    if root is None:  
        root = rbt_node.new_node(key, value)
        return root

    if key < root['key']: 
        root['left'] = insert_node(root['left'],  key, value)
    elif (key > root['key']): 
        root['right'] = insert_node(root['right'], key, value)
    else:
        if isinstance(root['value'],list):
            root['value'].append(value)
        else:
            x = root['value']
            root['value'] = [x]
            root['value'].append(value)
            
    if  (rbt_node.is_red(root['right']) and not (rbt_node.is_red(root['left']))):
        root = rotate_left(root)
    if(rbt_node.is_red(root['left']) and rbt_node.is_red(root['left']['left'])) :
        root = rotate_right(root)
    if (rbt_node.is_red(root['left']) and rbt_node.is_red(root['right'])):
        root['color'] = 0
        root['right']['color'] = 1
        root['left']['color'] = 1
    root['size'] = sizea(root['left']) + sizea(root['right']) + 1

    return root
def color(root):
    if root == None:
        return None
    if root['color'] == 0:
        root['color']== 1
    else:
        root['color'] = 0
def sizea(root):
    if root == None:
        return 0
    return root['size']

def rotate_left(root):
    x = root['right']
    root['right'] = x['left']
    x['left'] = root
    x['color'] = x['left']['color']
    x['left']['color'] = 0
    x['size'] = root['size']
    root['size'] = sizea(root['left']) + sizea(root['right']) + 1
    return x

def rotate_right(root):
    x = root['left']
    root['left'] = x['right']
    x['right'] = root
    x['color'] = x['right']['color']
    x['right']['color'] = 0
    x['size'] = root['size']
    root['size'] = sizea(root['left']) + sizea(root['right']) + 1
    return x

def get(my_rbt,key):
    if my_rbt['root'] is not None:
        if my_rbt['root']["key"] == key:
            return my_rbt['root']["value"]
        else:
            return get_node(my_rbt["root"],key)
            
        

def get_node(root,key):
       
    if root is not None:
        if key == root["key"]:
            return root["value"]
        elif key>root["key"]:
            return get_node(root["right"],key)
        elif key<root["key"] : 
             return get_node(root["left"],key)
    else:
        return None        

def remove(my_rbt, key):
    if my_rbt['root'] is not None:
        return remove_key(my_rbt['root'],key,my_rbt["root"])
        
def remove_key(root,key,original):
       
    if root is not None:
        if key == root["key"]:
            
            original["root"]["size"] -= 1
            if root["right"] is not None:
                root["key"] = root["right"]["key"]
                root["value"] = root["right"]["value"]
                root["size"] -= 1
                
                root["right"] = None
            else:
                root = None
                   
            return root
       
        elif key>root["key"]:
            root["right"] = remove_key(root["right"],key,original)
            return root
        elif key<root["key"] : 
             root["left"] = remove_key(root["left"],key,original)
             return root
    else:
        return root        
    
def contains(my_rbt,key):
    if get(my_rbt,key) is not None:
        return True
    else:
        return False

def size(my_bst):
    if my_bst["root"] is not None:
        return my_bst["root"]["size"]
    else:
        return 0

def is_empty(my_bst):
    if my_bst["root"] is not None:
        return False
    else:
        return True
def key_set(my_bst):

    rta = {'size':0, 'elements':[]}
    raiz = my_bst['root']
    key_set_tree(raiz,rta)
    return rta

def key_set_tree(raiz,lista):
    if raiz != None:
        lista['size'] += 1
        key_set_tree(raiz['left'],lista)
        lista["elements"].append(raiz['key'])
        key_set_tree(raiz['right'],lista)

def value_set(my_bst):

    rta = {'size':0, 'elements':[]}
    raiz = my_bst['root']
    value_set_tree(raiz,rta)
    return rta

def value_set_tree(raiz,lista):
    if raiz != None:
        lista['size'] += 1
        value_set_tree(raiz['left'],lista)
        lista["elements"].append(raiz['value'])
        value_set_tree(raiz['right'],lista)
        
def min_key(my_bst):
    if my_bst["root"] is not None:
        root = my_bst["root"]
        while root["left"] is not None:
            root = root["left"]
        return root["key"]
    else:
        return None
    
def max_key(my_bst):
    if my_bst["root"] is not None:
        root = my_bst["root"]
        max = root["key"]
        while root["right"] is not None:
            root = root["right"]
            if max < root["key"]:
                max = root["key"]
            
        return max
    else:
        return None
    
def floor_key(my_rbt,key,r):
    
    if my_rbt is not None:
        if my_rbt["key"]== key:
            return key
        elif my_rbt["key"]> key:
            return floor_key(my_rbt["left"],key,my_rbt)
        elif my_rbt["key"]<key:
            return floor_key(my_rbt["right"],key,my_rbt)
    else:
        if r["key"]<key:
            return r["key"]        
        else:
            return None
            
        
    
    
    
def floor(my_rbt,key):
    
    if my_rbt["root"] is not None:
        if my_rbt["root"]["key"] == key:
            return key
        else:
            return floor_key(my_rbt["root"],key,None)


    
def ceiling_key(my_rbt, key, r):
    if my_rbt is not None:
        if my_rbt["key"] == key:
            return key
        elif my_rbt["key"] > key:
           
            rta = ceiling_key(my_rbt["left"], key, my_rbt)
            if rta is not None:
                return rta
            else:
                return my_rbt["key"]
            
        else:  
            return ceiling_key(my_rbt["right"], key, r)
    else:
        if r is not None and r["key"] > key:
            return r["key"]
        else:
            return None

def ceiling(my_rbt, key):
    if my_rbt["root"] is not None:
        return ceiling_key(my_rbt["root"], key, None)
    else:
        return None
   

def select(my_bst,pos):
    if my_bst['root'] is None :
        return None
    l_llave = key_set(my_bst) 
    if pos >= l_llave['size']:
        return None
    rta = l_llave['elements'][pos]
    return rta

def rank(my_bst,key):
    if my_bst['root'] == None:
        return 0
    lis = key_set(my_bst)
    puesto = 0
    print(lis)
    while lis['elements'][puesto] < key:
        puesto += 1
        if puesto >= lis['size']:
            return puesto 
    return puesto

def keys(my_bst, key_lo, key_hi):
    rta = {'size':0,'elements':[]}
    if my_bst['root'] == None:
        return rta
    lis = key_set(my_bst)
    
    for key in lis['elements']:
        if key_lo <= key <= key_hi:
            rta['elements'].append(key)
            rta['size'] += 1
    return rta


def values(my_bst, key_lo, key_hi):
    rta = {'size':0,'elements':[]}
    if my_bst['root'] == None:
        return rta
    lis = key_set(my_bst)
    
    for key in lis['elements']:
        if key_lo <= key <= key_hi:
            rta['elements'].append(get(my_bst,key))
            rta['size'] += 1
    return rta

def height(my_bst):
    contar = 0
    if my_bst["root"] is not None:
        
        root = my_bst["root"]
        while root["right"] != None or root["left"] != None:
            contar += 1
            if root["right"] is not None:
                root = root["right"]
            elif root["left"] is not None:
                root = root["left"]
    
        return contar
    else:
        return -1
