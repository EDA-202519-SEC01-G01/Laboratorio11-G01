from DataStructures.Map import map_linear_probing as mp
from DataStructures.Priority_queue import priority_queue as pq

def new_dijsktra_structure(source, g_order):
    """
    Estructura de búsqueda usada en el algoritmo Dijkstra.
    """
    structure = {
        "source": source,
        "visited": mp.new_map(g_order, 0.5),
        "pq": pq.new_heap()
    }
    return structure
