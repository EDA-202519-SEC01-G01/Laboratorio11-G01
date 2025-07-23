from DataStructures.Map import map_linear_probing as mp

from DataStructures.Graph import vertex as ver

from DataStructures.Graph import edge as ed


def new_graph(order=0,):
    return {"vertices":mp.new_map(num_elements=14000, load_factor=0.7),
            "num_edges":0,
            "num_vertices":order}
    
def insert_vertex(my_graph,key,info):
    vertice=ver.new_vertex(key,info)    
    mp.put(my_graph["vertices"],key,vertice)
    my_graph["num_vertices"]+=1
    return my_graph

def update_vertex_info(my_graph,key,info):
    vertice=mp.get(my_graph["vertices"],key)["value"]
    
    ver.set_value(vertice,info)
    
    return my_graph

def remove_vertex(my_graph, key):

    vertices = mp.value_set(my_graph["vertices"])
    for vertex in vertices:
        if mp.contains(vertex["adjacents"], key):
            mp.remove(vertex["adjacents"], key)
            my_graph["num_edges"] -= 1
 
    mp.remove(my_graph["vertices"], key)
    my_graph["num_vertices"] -= 1
    return my_graph

def add_edge(my_graph, key1, key2, weight=1):

    vertice1 = mp.get(my_graph["vertices"], key1)
    print(vertice1)
    vertice2 = mp.get(my_graph["vertices"], key2)
    print(vertice1)
    
    if vertice1 and vertice2:
        ver.add_adjacent(vertice1, key2, weight)
        my_graph["num_edges"] += 1
        
    return my_graph

def order(my_graph):
    return my_graph["num_vertices"]

def size(my_graph):
    return my_graph["num_edges"]

def vertices(my_graph):
    return mp.key_set(my_graph["vertices"])

def degree(my_graph,key):
    vertice=mp.get(my_graph["vertices"],key)
    
    grado=ver.degree(vertice)
    
    return grado

def get_edge(my_graph, key1, key2):
    
    vertex_u = mp.get(my_graph["vertices"], key1)
    adjacents = vertex_u["adjacents"]
    edge = mp.get(adjacents, key2)

    return edge

def get_vertex_information(my_graph,key):
    vertice=mp.get(my_graph["vertices"],key)["value"]
    
    info=ver.get_value(vertice)
    
    return info

def contains_vertex(my_graph,key):
    return mp.contains(my_graph["vertices"],key)

def adjacents(my_graph,key):
    vertice=mp.get(my_graph["vertices"],key)["value"]
    
    rta=mp.key_set(vertice["adjacents"])
    
    return rta

def edges_vertex(my_graph, key1):
    if not mp.contains(my_graph["vertices"], key1):
        raise Exception(f"El vértice '{key1}' no existe en el grafo.")
    
    vertice = mp.get(my_graph["vertices"], key1)["value"]
    adyacentes = ver.get_adjacents(vertice)
    llaves_adyacentes = mp.key_set(adyacentes)

    rta = []

    for key2 in llaves_adyacentes:
        peso = mp.get(adyacentes, key2)
        arco = ed.new_edge(key2, peso)
        rta.append(arco)
    
    return rta

def get_vertex(my_graph,key):
    vertice=mp.get(my_graph["vertices"],key)
    
    return vertice


    

