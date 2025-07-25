from DataStructures.List import array_list as lt
from DataStructures.Priority_queue import index_pq_entry as pqe

def new_heap(is_min_pq=True):
    heap = {
        "elements": lt.new_list(),
        "size": 0,
        "cmp_function": default_compare_lower_value if is_min_pq else default_compare_higher_value
    }
    lt.add_last(heap["elements"], None)
    return heap

def default_compare_higher_value(father_node, child_node):
    return pqe.get_key(father_node) >= pqe.get_key(child_node)

def default_compare_lower_value(father_node, child_node):
    return pqe.get_key(father_node) <= pqe.get_key(child_node)

def priority(my_heap, parent, child):
    return my_heap["cmp_function"](parent, child)

def swim(my_heap):
    i = my_heap["size"]
    while i > 1:
        padre = i // 2
        parent = lt.get_element(my_heap["elements"], padre)
        child = lt.get_element(my_heap["elements"], i)
        if not my_heap["cmp_function"](parent, child):
            lt.exchange(my_heap["elements"], padre, i)
            i = padre
        else:
            break

def sink(my_heap):
    i = 1
    while 2 * i <= my_heap["size"]:
        j = 2 * i
        if j < my_heap["size"]:
            left = lt.get_element(my_heap["elements"], j)
            right = lt.get_element(my_heap["elements"], j + 1)
            if not my_heap["cmp_function"](left, right):
                j += 1
        parent = lt.get_element(my_heap["elements"], i)
        child = lt.get_element(my_heap["elements"], j)
        if my_heap["cmp_function"](parent, child):
            break
        lt.exchange(my_heap["elements"], i, j)
        i = j

def insert(my_heap, key, value):
    entrada = pqe.new_pq_entry(key, value)
    my_heap["size"] += 1
    pqe.set_index(entrada, my_heap["size"])
    lt.add_last(my_heap["elements"], entrada)
    swim(my_heap)
    return my_heap
def size(my_heap):
    return my_heap["size"]

def is_empty(my_heap):
    return my_heap["size"] == 0

def get_first_priority(my_heap):
    if my_heap["size"] == 0:
        return None
    elemento = lt.get_element(my_heap["elements"], 1)
    return elemento["key"]

def remove(my_heap):
    if my_heap["size"] == 0:
        return None
    lt.exchange(my_heap["elements"], 1, my_heap["size"])
    eliminado = lt.remove_last(my_heap["elements"])
    my_heap["size"] -= 1
    sink(my_heap)
    return eliminado["key"]