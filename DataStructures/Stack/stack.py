from DataStructures.List import single_linked_list as sl

def new_stack():
    stack=sl.new_list()
    return stack

def is_empty(my_stack):
    if my_stack["size"]==0:
        return True
    else:
        return False

def size(my_stack):
    return my_stack["size"]

def push(my_stack,element):
    return sl.add_first(my_stack,element)

def pop(my_stack):
    return sl.remove_first(my_stack)

def top(my_stack):
    return sl.first_element(my_stack)
    
        