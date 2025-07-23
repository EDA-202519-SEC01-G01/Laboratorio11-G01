from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
import random as rd
from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as al
from DataStructures.Tree import rbt_node as Node

def new_map():
    return {"root":None,"type":"RBT","size":0}

def rotIzq(nodo):
        nova=nodo["right"]
        desc=nova["left"]
        nova["left"]=nodo
        nodo["right"]=desc
        nova["color"]=nodo["color"]
        nodo["color"]=Node.RED
        return nova
    
def rotDer(nodo):
        nova=nodo["left"]
        desc=nova["right"]
        nova["right"]=nodo
        nodo["left"]=desc
        nova["color"]=nodo["color"]
        nodo["color"]=Node.RED
        return nova
    
def swap(nodo):
    nodo["color"]=Node.RED
    nodo["left"]["color"]=Node.BLACK
    nodo["right"]["color"]=Node.BLACK
    
def rotar(nodo):
    if nodo["right"] is not None and nodo["right"]["color"] == Node.RED and (nodo["left"] is None or nodo["left"]["color"] != Node.RED):
        nodo = rotIzq(nodo)
    if nodo["left"] is not None and nodo["left"]["color"] == Node.RED and nodo["left"].get("left") and nodo["left"]["left"]["color"] == Node.RED:
        nodo = rotDer(nodo)
    if nodo["left"] is not None and nodo["right"] is not None and nodo["left"]["color"] == Node.RED and nodo["right"]["color"] == Node.RED:
        swap(nodo)
    return nodo

def get(my_rbt,key):
        return get_node(my_rbt["root"],key)
def get_node(root,key): #O(n)/O(log(n))
        if root==None:
            return None
        elif key==root["key"]:
            return root["value"]
        elif root["key"]<key:
            return get_node(root["right"],key)
        else:
            return get_node(root["left"],key)
        
def put(my_bst,key,value):
    if my_bst["root"]==None:
        my_bst["root"]=Node.new_node(key,value)
        if "size" in my_bst:
            my_bst["size"]+=1
    else:
        my_bst["root"],añadir=insert_node(my_bst["root"],key,value)
        if añadir:
            if "size" in my_bst:
                my_bst["size"]+=1   
        my_bst["root"]["color"]=Node.BLACK
    return my_bst
def insert_node(root,key,value):
    if root==None:
        root=Node.new_node(key,value)
        return root,True
    elif key==root["key"]:
        root["value"]=value
        return root,False
    elif key > root["key"]:
        root["right"],añadir=insert_node(root["right"],key,value)
    else:
        root["left"],añadir=insert_node(root["left"],key,value)
    root=rotar(root)
    root["size"] = 1 + size_node(root["left"]) + size_node(root["right"])

    return root,añadir

def size_node(node):
    if node is None:
        return 0
    return node["size"]

def rotate_left(h):
    x = h["right"]
    h["right"] = x["left"]
    x["left"] = h
    x["color"] = h["color"]
    h["color"] = True
    x["size"] = h["size"]
    h["size"] = 1 + size_node(h["left"]) + size_node(h["right"])
    return x

def rotate_right(h):
    x = h["left"]
    h["left"] = x["right"]
    x["right"] = h
    x["color"] = h["color"]
    h["color"] = True
    x["size"] = h["size"]
    h["size"] = 1 + size_node(h["left"]) + size_node(h["right"])
    return x

def flip_colors(h):
    h["color"] = True
    if h["left"] is not None:
        h["left"]["color"] = False
    if h["right"] is not None:
        h["right"]["color"] = False


def remove(my_bst,key):
    my_bst["root"],remover=remove_node(my_bst["root"],key)
        
    if remover:
        if "size" in my_bst:
            my_bst["size"]+=1
    
    return my_bst

def remove_node(nodo,key):
        if nodo==None:
            return None,False
        elif nodo["key"]<key:
            nodo["right"],remover=remove_node(nodo["right"],key)
        elif nodo["key"]>key:
            nodo["left"],remover=remove_node(nodo["left"],key)
        else:
            if nodo["left"]==None and nodo["right"]==None:
                return None,True
            elif nodo["left"]==None:
                return nodo["right"],True
            elif nodo["right"]==None:
                return nodo["left"],True
            else:
                heir=minimo(nodo.right)
                nodo["right"],remover=remove_node(nodo["right"],heir["key"])
                heir["left"]=nodo["left"]
                heir["right"]=nodo["right"]
                return heir,True
        nodo = rotar(nodo)
        
        return nodo, remover
    
def maximo(nodo):
        rta=nodo
        while rta["right"]!=None:
            rta=rta["right"]
        return rta
    
def contains(my_rbt,key):
    if get(my_rbt,key):
        return True
    else:
        return False
    
def minimo(nodo):
        rta=nodo
        while rta["left"]!=None:
            rta=rta["left"]
        return rta

def get_min_node(node):
    while node["left"] is not None:
        node = node["left"]
    return node

def size(my_rbt):
    if my_rbt["root"]:
        return my_rbt["size"]
    else:
        return 0

def is_empty(my_rbt):
    if my_rbt["root"]:
        return False
    else:
        return True
    
def key_set(my_bst):
    rta = al.new_list()
    rta = order(my_bst["root"], rta, "key")  
    return rta

    return rta
def key_set_tree(root, key_list):
    if root is not None:
        key_set_tree(root["left"], key_list)
        al. add_last(key_list, root["key"])
        key_set_tree(root["right"], key_list)
    return key_list

def value_set(my_bst):

    rta=sl.new_list()
    rta=order(my_bst["root"],rta,"value")
        
    return rta
    
def order(nodo, array, crit):
    if nodo is not None:
        order(nodo["right"], array, crit)
        al.add_last(array, nodo[crit])
        order(nodo["left"], array, crit)
    return array

def orderj(nodo,array,crit):
    if nodo!=None:
        order(nodo["right"],array)
        al.add_last(array,nodo[crit])
        order(nodo["left"],array)
    return array

def get_min(my_rbt):
    if my_rbt["root"]:
        return minimo(my_rbt["root"])["key"]
    else:
        return None
    
def get_max(my_rbt):
    if my_rbt["root"]:
        return maximo(my_rbt["root"])["key"]
    else:
        return None
    
def delete_min(my_rbt):
    muerto=get_min(my_rbt)
    my_rbt=remove(my_rbt,muerto)
    return my_rbt

def delete_max(my_rbt):
    muerto=get_max(my_rbt)
    my_rbt=remove(my_rbt,muerto)
    return my_rbt


def floor(my_rbt,key):
    if contains(my_rbt,key):
        return key
    else:
        return floor_key(my_rbt["root"],key)
        
def floor_key(nodo,key):
    if nodo is None:
        return None
    elif key < nodo["key"]:
        return floor_key(nodo["left"], key)
    
    else:
        temp = floor_key(nodo["right"], key)
        if temp is not None:
            return temp 
    return(nodo["key"])
def ceiling(my_rbt, key):
    node = ceiling_key(my_rbt["root"], key)
    if node is None:
        return None
    return node["key"]
def ceiling_key(root, key):
    if root is None:
        return None

    if key == root["key"]:
        return root

    if key > root["key"]:
        return ceiling_key(root["right"], key)

    temp = ceiling_key(root["left"], key)
    if temp is not None:
        return temp
    else:
        return root
def select(my_rbt, pos):
    node = select_key(my_rbt["root"], pos)
    if node is None:
        return None
    return node["key"]
def select_key(root, pos):
    if root is None:
        return None

    left_size = size_node(root["left"])

    if pos < left_size:
        return select_key(root["left"], pos)
    elif pos > left_size:
        return select_key(root["right"], pos - left_size - 1)
    else:
        return root
def rank(my_rbt, key):
    return rank_keys(my_rbt["root"], key)
def rank_keys(root, key):
    if root is None:
        return 0

    if key < root["key"]:
        return rank_keys(root["left"], key)
    elif key > root["key"]:
        left_size = size_node(root["left"])
        return 1 + left_size + rank_keys(root["right"], key)
    else:
        return size_node(root["left"])
def height(my_rbt):
    return height_tree(my_rbt["root"])
def height_tree(root):
    if root is None:
        return 0
    return 1 + max(height_tree(root["left"]), height_tree(root["right"]))
def keys(my_rbt, key_initial, key_final):
    key_list = sl.new_list()
    keys_range(my_rbt["root"], key_initial, key_final, key_list)
    return key_list
def keys_range(root, key_initial, key_final, list_key):
    if root is None:
        return

    if key_initial < root["key"]:
        keys_range(root["left"], key_initial, key_final, list_key)

    if key_initial <= root["key"] <= key_final:
        sl. add_last(list_key, root["key"])

    if key_final > root["key"]:
        keys_range(root["right"], key_initial, key_final, list_key)
        
        
def keys_al(my_rbt, key_initial, key_final):
    key_list = al.new_list()
    keys_range_al(my_rbt["root"], key_initial, key_final, key_list)
    return key_list
def keys_range_al(root, key_initial, key_final, list_key):
    if root is None:
        return

    if key_initial < root["key"]:
        keys_range_al(root["left"], key_initial, key_final, list_key)

    if key_initial <= root["key"] <= key_final:
        al. add_last(list_key, root["key"])

    if key_final > root["key"]:
        keys_range_al(root["right"], key_initial, key_final, list_key)
        
        
def values(my_rbt, key_initial, key_final):
    value_list = al.new_list()
    return values_range(my_rbt["root"], key_initial, key_final, value_list)

def values_range(root, key_initial, key_final, value_list):
    if root is None:
        return value_list

    if key_initial < root["key"]:
        value_list = values_range(root["left"], key_initial, key_final, value_list)

    if key_initial <= root["key"] <= key_final:
        al.add_last(value_list, root["value"])

    if key_final > root["key"]:
        value_list = values_range(root["right"], key_initial, key_final, value_list)

    return value_list




def rotate_left(node_rbt):
    x = node_rbt["right"]
    node_rbt["right"] = x["left"]
    x["left"] = node_rbt
    x["color"] = node_rbt["color"]
    node_rbt["color"] = True
    x["size"] = node_rbt["size"]
    node_rbt["size"] = 1 + size_node(node_rbt["left"]) + size_node(node_rbt["right"])
    return x
def rotate_right(node_rbt):
    x = node_rbt["left"]
    node_rbt["left"] = x["right"]
    x["right"] = node_rbt
    x["color"] = node_rbt["color"]
    node_rbt["color"] = True
    x["size"] = node_rbt["size"]
    node_rbt["size"] = 1 + size_node(node_rbt["left"]) + size_node(node_rbt["right"])
    return x
def flip_node_color(node_rbt):
    node_rbt["color"] = not node_rbt["color"]
    return node_rbt
def flip_colors(node_rbt):
    node_rbt["color"] = not node_rbt["color"]
    if node_rbt["left"]:
        node_rbt["left"]["color"] = not node_rbt["left"]["color"]
    if node_rbt["right"]:
        node_rbt["right"]["color"] = not node_rbt["right"]["color"]
    return node_rbt
def is_red(node_rbt):
    if node_rbt is None:
        return False
    return node_rbt["color"]
def size_tree(root):
    if root is None:
        return 0
    return root["size"]
def move_red_right(root):
    flip_colors(root)
    if is_red(root["left"]["left"]):
        root = rotate_right(root)
        flip_colors(root)
    return root
def move_red_left(root):
    flip_colors(root)
    if is_red(root["right"]["left"]):
        root["right"] = rotate_right(root["right"])
        root = rotate_left(root)
        flip_colors(root)
    return root
def balance(root):
    if is_red(root["right"]) and not is_red(root["left"]):
        root = rotate_left(root)
    if is_red(root["left"]) and is_red(root["left"]["left"]):
        root = rotate_right(root)
    if is_red(root["left"]) and is_red(root["right"]):
        flip_colors(root)

    root["size"] = 1 + size_node(root["left"]) + size_node(root["right"])
    return root
def default_compare(key, element):
    if key == element["key"]:
        return 0
    elif key > element["key"]:
        return 1
    else:
        return -1


def print_rbt_tree(node, indent="", last=True):
    if node is not None:
        color = "R" if node["color"] else "B"
        print(indent + ("└── " if last else "├── ") + f"{node['key']} ({color})")
        indent += "    " if last else "│   "
        children = [node["left"], node["right"]]
        if children[0] is not None or children[1] is not None:
            if children[1] is not None:
                print_rbt_tree(children[0], indent, False)
                print_rbt_tree(children[1], indent, True)
            else:
                print_rbt_tree(children[0], indent, True)
                
                
def print_rbt_tree_vertical(node, level=0, prefix="Root: "):
    if node is not None:
        print_rbt_tree_vertical(node["right"], level + 1, "R── ")
        
        indent = "     " * level
        color = "R" if node.get("color", True) else "B"
        print(f"{indent}{prefix}{node['key']} ({color})")
        
        print_rbt_tree_vertical(node["left"], level + 1, "L── ")