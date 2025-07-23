from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
import random as rd
from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as al


def new_map(num_elements, load_factor, prime=109345121):
    my_map = {
        'prime': prime,
        'capacity': mf.next_prime(num_elements / load_factor),
        'scale': rd.randint(1, prime - 1),
        'shift': rd.randint(0, prime - 1),
        'table': al.new_list(),
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0
    }

    for _ in range(my_map['capacity']):
        al.add_last(my_map['table'], sl.new_list()) #es lista nodal por lo que es linked list por lo que toca guardar cositas si llegan haber colisiones estas cositas son nodos ojo

    return my_map


def put(my_map, key, value):
    
    new_entry = me.new_map_entry(key, value)
    pos = mf.hash_value(my_map, key)
    lista_an = al.get_element(my_map['table'], pos)  # Lista enlazada a donde debe ir 

    # Buscar si ya existe una entrada con esa llave
    for i in range(sl.size(lista_an)):
        nodo_act = sl.get_element(lista_an, i) #miramos los noditos de ese sll que estamos parados, una sll tiene info ahi cogimos fue la info 
        if me.get_key(nodo_act) == key: #info tiene {key: x , value: xx} entonces miramos la key si es igual pues lo remplazo normal
            me.set_value(nodo_act, value)  # si existe o sea es la misma, solo remplazamos el valor (fue litaral como que borre la anterior porque le mande una nueva)
            return my_map

    # Si no existe osea no hay llaves que sobreescrir literal , se agrega una nueva entrada al final
    sl.add_last(lista_an, new_entry)
    my_map['size'] += 1
    my_map['current_factor'] = my_map['size'] / my_map['capacity']

    # Si se pasa el factor de carga, hacemos rehash
    if my_map['current_factor'] > my_map['limit_factor']:
        my_map = rehash(my_map)

    return my_map



def default_compare(key, element):

   if (key == me.get_key(element)):
      return 0
   elif (key > me.get_key(element)):
      return 1
   return -1


def contains(my_map, key):
    pos = mf.hash_value(my_map, key)
    lista_an = al.get_element(my_map['table'], pos) # me paro en la posicion del arreglo despues de hashear esta  tiene una sll y agarro esa listica anidada

    for i in range(sl.size(lista_an)):
        nodo = sl.get_element(lista_an, i) #miro el key de cada node porque ahi estoy viendo es { key:x , value:xx }
        if me.get_key(nodo) == key:
            return True

    return False



def remove(my_map, key):
    pos = mf.hash_value(my_map, key)
    lista_an = al.get_element(my_map['table'], pos) #me paro en la sll que es la pos despues de hashear la key

    for i in range(sl.size(lista_an)):
        nodo = sl.get_element(lista_an, i) #miro el key de cada node porque ahi estoy viendo es { key:x , value:xx }
        if me.get_key(nodo) == key: # si {key:x} coincidecon la key del parametro, pues entra borrarlo
            sl.delete_element(lista_an, i)
            my_map['size'] -= 1
            my_map['current_factor'] = my_map['size'] / my_map['capacity']
            return my_map

    return my_map

def get(my_map, key):
    pos = mf.hash_value(my_map, key)
    lista_an = al.get_element(my_map['table'], pos)
    
    for i in range(sl.size(lista_an)):
        nodo = sl.get_element(lista_an, i)
        if me.get_key(nodo) == key:
            return me.get_value(nodo)
        
    return None

def key_set(my_map):
    elementos = my_map["table"]["elements"]
    lista_llaves = al.new_list()
    
    for dato in elementos:
        temp = dato['first']
        while temp is not None:
            if me.get_key(temp['info']) is not None and me.get_key(temp['info']) is not "__EMPTY__": 
                al.add_last(lista_llaves, me.get_key(temp['info']))
            temp = temp['next']
    
    return lista_llaves

def value_set(my_map):
    elementos = my_map["table"]["elements"]
    lista_valores = al.new_list()
    
    for dato in elementos:
        temp = dato['first']
        while temp is not None:
            if me.get_value(temp['info']) != None and me.get_value(temp['info']) != "__EMPTY__": 
                al.add_last(lista_valores, me.get_value(temp['info']))
            
            temp = temp['next']
            
    
    return lista_valores

def size(my_map):
    return my_map['size']

def is_empty(my_map):
    return size(my_map) == 0

def rehash(my_map):
    load_factor = my_map["limit_factor"]
    prime = my_map["prime"]
    vieja_tabla = my_map["table"]

    
    nuevo_mapa = new_map(my_map["capacity"] * 2, load_factor, prime)

    for lista in vieja_tabla["elements"]:
        temp = lista["first"]
        while temp is not None:
            key = me.get_key(temp["info"])
            value = me.get_value(temp["info"])
            put(nuevo_mapa, key, value)
            temp = temp["next"]

    my_map["capacity"] = nuevo_mapa["capacity"]
    my_map["table"] = nuevo_mapa["table"]
    my_map["scale"] = nuevo_mapa["scale"]
    my_map["shift"] = nuevo_mapa["shift"]
    my_map["size"] = nuevo_mapa["size"]
    my_map["current_factor"] = nuevo_mapa["current_factor"]

    return my_map
                

    