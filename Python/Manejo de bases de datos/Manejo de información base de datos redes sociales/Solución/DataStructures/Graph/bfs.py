from DataStructures.Graph import adj_list_graph as gl
from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as lt
from DataStructures.Graph import edge
from DataStructures.Stack import stack as stk
from DataStructures.Queue import queue as qu


def breath_first_search(my_graph, source):
    cola = qu.new_queue()
    vertices = gl.vertices(my_graph)
    search = {'source':source, 'visited':None}
    search['visited'] = mp.new_map(vertices['size'],load_factor=0.5)
    mp.put(search['visited'],source,{'marked':True,'edge_to':None,'dist_to':0})
    qu.enqueue(cola,source)
    while qu.size(cola)>0:
        actual = qu.dequeue(cola)
        info = mp.get(my_graph['vertices'], actual)
        if info != None:
            for dic in info:
                v = dic['vertex_b']
                if v != None :
                    x= mp.get(search['visited'],v)
                    if x == None or x['marked'] == False:
                        qu.enqueue(cola,v)
    return search    
def has_path_to(search, vertex):
    if vertex == search['source']:
        return True
    pos = (((search['visited']['scale'] * hash(vertex)) + search['visited']['shift']) % search['visited']['prime']) % search['visited']['capacity']
    v = search['visited']['table'][pos]

    if v == None:
        return False
    for dic in v:
        if vertex in dic.keys():
            d= dic
    if  d[vertex]['edge_to'] != None:
        return has_path_to(search, d[vertex]['edge_to'])
    
    return False


def path_to(search,vertex):
    stack = stk.new_stack()
    rta = path(search,vertex,stack)
    print(rta)
    return rta

def path(search,vertex,stack):
    if vertex == search['source']:
        stk.push(stack,vertex)
        return stack
    pos = (((search['visited']['scale'] * hash(vertex)) + search['visited']['shift']) % search['visited']['prime']) % search['visited']['capacity']
    v = search['visited']['table'][pos]

    if v == None:
        return False
    for dic in v:
        if vertex in dic.keys():
            d= dic
    if  d[vertex]['edge_to'] != None:
        stk.push(stack,vertex)
        path(search,d[vertex]['edge_to'],stack)
        return stack
    else:
    
        return False
     

    
    
