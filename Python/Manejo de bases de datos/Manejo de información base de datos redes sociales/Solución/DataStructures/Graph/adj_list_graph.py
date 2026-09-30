from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import edge as edge
from DataStructures.List import array_list as lt



def new_graph(size=3000,directed=False):
    rta = {'edges':0,
           'in_degree':None,
           'vertices': mp.new_map(size,0.5),
            'information':mp.new_map(size,0.5),
            'directed': directed,
            'type': "ADJ_LIST"}
    return rta

def insert_vertex(graph,key_vertex,vert,info_vertex):
    
    mp.put(graph['information'],key_vertex,info_vertex)
    ed_v = edge.new_edge(key_vertex,vert, 3.0)
    edges = [ed_v]
    mp.put(graph["vertices"],key_vertex,edges )
        
    return graph
def num_vertices(graph):
    return mp.size(graph['vertices'])

def add_edge(graph, vertex_a, vertex_b, weight=0):
    x = edge.new_edge(vertex_a, vertex_b, weight)

    # Verifica si el vértice está presente
    if mp.get(graph['vertices'], vertex_a) is not None:
        pos = (((graph['vertices']['scale'] * abs(hash(vertex_a))) + graph['vertices']['shift']) % graph['vertices']['prime']) % graph['vertices']['capacity']
        if graph['vertices']['table'][pos] is None:
            graph['vertices']['table'][pos] = [{}]
        if vertex_a not in graph['vertices']['table'][pos][0]:
            graph['vertices']['table'][pos][0][vertex_a] = []
        graph['vertices']['table'][pos][0][vertex_a].append(x)

        
                
def num_edges(graph) :
    x = mp.value_set(graph['vertices'])
    rta = round((lt.size(x))/2)
    return rta
def degree(my_graph,key_vertex):
    x = mp.get(my_graph['vertices'],key_vertex)
    rta = None
    if x != None:
        rta = x['size']
    return rta

def vertices(my_graph):
    rta = mp.key_set(my_graph['vertices'])
    return rta
def compara(ed1,ed2):
    rta = False
    if isinstance(ed1,list):
        ed1 = ed1[0]
    if isinstance(ed2,list):
        ed2 = ed2[0]
    if ed1['vertex_a'] == ed2['vertex_b'] and (ed2['vertex_a'] == ed1['vertex_b']):
        rta = True 
    return rta
def edges(my_graph):
    edges = mp.value_set(my_graph['vertices'])
    arcos = lt.new_list()
    for lista in edges['elements']:
        for arc in lista:
            prob = True
            arc
            for a in arcos['elements']:
                
                if compara(arc,a) :
                    prob = False
            
            if prob:
                arcos['elements'].append(arc)
                arcos['size'] += 1
    return arcos["size"]
    


def in_degree(my_graph, key_vertex):
    x = mp.get(my_graph['vertices'],key_vertex)
    rta = None
    if x != None:
        rta = x['size']
    return rta
def get_edge(graph,vertex_a,vertex_b):
    pass

def contains_vertex(graph,vertex):
    pass    