from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
import random as rd
from DataStructures.List import array_list as al



def new_map(num_elements, load_factor, prime=109345121):
    my_map ={
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
        al.add_last(my_map['table'], me.new_map_entry(None, None))
    
    return my_map
        
        
def put(my_map, key, value):
    
    new_entry = me.new_map_entry(key, value)
    pos = mf.hash_value(my_map, key)
    ocupied, slot = find_slot(my_map, key, pos)
    
    if ocupied:
        current_entry = al.get_element(my_map['table'], slot) #este es cuando ya esta, solo le remplazamos el valor para que no se nos vaya por alla a lagun lado raro
        me.set_value(current_entry, value)
        al.change_info(my_map['table'], slot, current_entry)
    else:
        al.change_info(my_map['table'], slot, new_entry)
        my_map['size'] += 1
        my_map['current_factor'] = my_map['size'] / my_map['capacity'] # cuando no esta y toca sumarle y a demas cambiar el current factor ojo 
        
        if my_map['current_factor'] > my_map['limit_factor']:
            my_map = rehash(my_map)  #si se pasa hacer rehash por que le perecio pequeño al señor
        
        
    return my_map

def remove(my_map, key):
    
    indexhasheado = mf.hash_value(my_map, key)
    elementos = my_map["table"]["elements"]

    for _ in range(my_map["capacity"]):
        
        if elementos[indexhasheado] is None: #para si hay un none para que no itere como loko
            break 

        if  me.get_key(elementos[indexhasheado]) == key:
            me.set_key(elementos[indexhasheado], "__EMPTY__") # cambiamos la llave a empty
            me.set_value(elementos[indexhasheado], "__EMPTY__")#lo mismo pero ahora el valor
            my_map["size"] -= 1
            my_map["current_factor"] = my_map["size"] / my_map["capacity"] # actualizo el current factor porque quite cositas
            break

        indexhasheado = (indexhasheado + 1) % my_map["capacity"] #avanzo teneindo en cuanta que no me púedo salir del size

    return my_map


def get(my_map, key):
    for i in range(my_map['capacity']):
        if me.get_key(my_map['table']['elements'][i]) == key:
            entry = my_map['table']['elements'][i]
            return me.get_value(entry)
    
    return None
    
    
def size(my_map):
    return my_map["size"] #el size nos da lo que se esta usando tipo lo que tiene data y ya


def is_empty(my_map):
    
    if size(my_map) == 0:
        return True
    else:
        return False
    
    
def key_set(my_map):
    elementos = my_map["table"]["elements"]
    lista_llaves = al.new_list()

    for dato in elementos:
        if dato != None: # verifico que no sea nada primero osea obviamente
            llave = me.get_key(dato)
            if llave != None and llave != "__EMPTY__": #verifico que la LLAVE no sea ni none ni empty....
                al.add_last(lista_llaves, llave)

    return lista_llaves

def value_set(my_map):
    
    lista_valores= al.new_list()
    mapitas = my_map["table"]["elements"]
    
    for mapa_act in mapitas:
        if mapa_act != None:
            valor = me.get_value(mapa_act)
            if valor != None and valor != "__EMPTY__": #NO ES NI NONE NI EMPTY? SI SI PASA!!! , SI NO, CHAOoOoO
                al.add_last(lista_valores, valor)
    return lista_valores


def find_slot(my_map, key, hash_value):
    first_avail = None
    found = False
    ocupied = False
    while not found:
        if is_available(my_map["table"], hash_value):
                if first_avail is None:
                    first_avail = hash_value
                entry = al.get_element(my_map["table"], hash_value)
                if me.get_key(entry) is None:
                    found = True
        elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
                first_avail = hash_value
                found = True 
                ocupied = True #son iguales solo remplazo y yaa para que no hayan duplicados lol
        hash_value = (hash_value + 1) % my_map["capacity"]
    return ocupied, first_avail
    
    
    
def is_available(table, pos):
    
    entry = al.get_element(table, pos)
    if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
        return True
    
    return False



def rehash(my_map):
    
    num_elements = mf.next_prime(my_map["capacity"] * 2) #cambiamos el tamaño a el doble y ademas es el siguiente primo mas grande
    load_factor = my_map["limit_factor"] #el mismo de todooo siempreeeee
    primo_default = my_map["prime"] #el mismo porque o si no re paila el calculo del hasheo
    
    nuevo_map = new_map(num_elements, load_factor,primo_default ) # creamos el nuevo mapa porque el otro le quedo pequeño 
    
    lista_elements = my_map["table"]["elements"] #vamos a la lista de cositas
    
    for element in lista_elements: #miramos esa lista de cositas
        if element != None:
            key = me.get_key(element) #cogemos el valor de esa llave donde estemos parados
            if key != None and key != "__EMPTY__":
                value = me.get_value(element) #element es el dict en el que estamos parados entonces a ese element le cogemos el value facilmente porque get value lo coge solo
                put(nuevo_map, key, value) #se lo metemos al nuevo maaappp obvio tiene que cumplir con que              
    
    return nuevo_map
    
    
    

def default_compare(key, entry):
    if key == me.get_key(entry):
      return 0
    elif key > me.get_key(entry):
      return 1
    
    return -1





def contains(my_map, key):
    
    valorsito = mf.hash_value(my_map,key)
    si_no,indice = find_slot(my_map, key, valorsito)
    
    if si_no == True and my_map["table"]["elements"][indice]["key"] == key:
            return True
    else:
        return False


    
    