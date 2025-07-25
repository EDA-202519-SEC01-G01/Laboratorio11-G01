from DataStructures.Queue import queue
from DataStructures.Map import map_linear_probing as map


def new_bfs_structure(g_order):
    """
    Crea una estructura de búsqueda para BFS.
    
    :param g_order: Número total de vértices en el grafo.
    :return: Estructura bfs_search inicializada.
    """
    bfs_structure = {
        'marked': None,            
        'dist_to': None,             
        'edge_to': None,            
        'order': queue.new_queue()                 
    }


    bfs_structure["marked"] = map.new_map(
    num_elements=g_order, 
    load_factor=0.5)

    bfs_structure["dist_to"] = map.new_map(
    num_elements=g_order,
    load_factor=0.5)

    bfs_structure["edge_to"] = map.new_map(
    num_elements=g_order,
    load_factor=0.5)

    return bfs_structure
   
    


