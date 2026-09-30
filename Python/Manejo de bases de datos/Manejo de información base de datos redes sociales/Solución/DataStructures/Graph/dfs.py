from DataStructures.Graph import adj_list_graph as gl
from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as lt
from DataStructures.Graph import edge
from DataStructures.Stack import stack as stk

def depth_first_search(my_graph, source):
    vertices = gl.vertices(my_graph)
    search = {'source':source, 'visited':None}
    search['visited'] = mp.new_map(vertices['size'],load_factor=0.5)
    mp.put(search['visited'],source,{'marked':True,'edge_to':None})
    dfs_vertex(search,my_graph,source)
    return search

def dfs_vertex(search, graph, source):
    info = mp.get(graph['vertices'], source)
    if info == None or not isinstance(info, list):
        return None  

    for dic in info:
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
     

    
    
