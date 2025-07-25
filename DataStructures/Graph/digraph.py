from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import vertex as ver
from DataStructures.Graph import edge as ed

def new_graph(order=0):
    return {
        "vertices": mp.new_map(num_elements=order, load_factor=0.7),
        "num_edges": 0,
        "num_vertices": 0
    }

def insert_vertex(my_graph, key, info):
    if not mp.contains(my_graph["vertices"], key):
        vertice = ver.new_vertex(key, info)
        mp.put(my_graph["vertices"], key, vertice)
        my_graph["num_vertices"] += 1
        print(f"[VERTEX_ADDED] {key} | total_vertices={my_graph['num_vertices']}")
    else:
        print(f"[VERTEX_EXISTS] {key} ya estaba")
    return my_graph


def update_vertex_info(my_graph, key, info):
    vertice = mp.get(my_graph["vertices"], key)["value"]
    ver.set_value(vertice, info)
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
    v1 = mp.get(my_graph["vertices"], key1)
    v2 = mp.get(my_graph["vertices"], key2)

    print(f"[VERTEX_CHECK] key1={key1} -> {'OK' if v1 else 'MISSING'} | key2={key2} -> {'OK' if v2 else 'MISSING'}")

    if v1 is not None and v2 is not None:
        vertice1 = v1["value"]
        adj_map = ver.get_adjacents(vertice1)

        if not mp.contains(adj_map, key2):  # solo si el arco no está
            ver.add_adjacent(vertice1, key2, weight)
            my_graph["num_edges"] += 1
            print(f"[EDGE_ADDED] {key1} -> {key2} (peso={weight}) | total_edges={my_graph['num_edges']}")
        else:
            print(f"[EDGE_EXISTS] {key1} -> {key2} ya existía")
    else:
        print(f"[EDGE_FAIL] No se pudo añadir: {key1} -> {key2}")

    return my_graph





def order(my_graph):
    return my_graph["num_vertices"]

def size(my_graph):
    return my_graph["num_edges"]

def vertices(my_graph):
    return mp.key_set(my_graph["vertices"])

def degree(my_graph, key):
    vertice = mp.get(my_graph["vertices"], key)["value"]
    return ver.degree(vertice)

def get_edge(my_graph, key1, key2):
    vertex_u = mp.get(my_graph["vertices"], key1)["value"]
    adjacents = ver.get_adjacents(vertex_u)
    return mp.get(adjacents, key2)

def get_vertex_information(my_graph, key):
    vertice = mp.get(my_graph["vertices"], key)["value"]
    return ver.get_value(vertice)

def contains_vertex(my_graph, key):
    return mp.contains(my_graph["vertices"], key)

def adjacents(my_graph, key):
    vertice = mp.get(my_graph["vertices"], key)["value"]
    return mp.key_set(ver.get_adjacents(vertice))

def edges_vertex(my_graph, key1):
    if not mp.contains(my_graph["vertices"], key1):
        raise Exception(f"El vértice '{key1}' no existe en el grafo.")
    vertice = mp.get(my_graph["vertices"], key1)["value"]
    adyacentes = ver.get_adjacents(vertice)
    llaves_adyacentes = mp.key_set(adyacentes)
    rta = []
    for key2 in llaves_adyacentes:
        edge_data = mp.get(adyacentes, key2)
        arco = ed.new_edge(key2, ed.weight(edge_data))
        rta.append(arco)
    return rta

def get_vertex(my_graph, key):
    found = mp.get(my_graph["vertices"], key)
    if found:
        return found["value"]
    return None
