from DataStructures.Queue import queue
from DataStructures.Map import map_linear_probing as map


def new_bfs_structure(g_order):
    """
    Crea una estructura de búsqueda para BFS.
    
    :param g_order: Número total de vértices en el grafo.
    :return: Estructura bfs_search inicializada.
    """
    bfs_structure = {
        'marked': map.new_map(num_elements=g_order, load_factor=0.5),
        'dist_to': map.new_map(num_elements=g_order, load_factor=0.5),
        'edge_to': map.new_map(num_elements=g_order, load_factor=0.5),
        'order': queue.new_queue()
    }

    return bfs_structure



