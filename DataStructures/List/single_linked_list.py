def new_list():
    my_list = {
        
        "first": None,
        "last": None,
        "size": 0
    }
    return my_list
def add_first(my_list, element):
    new_node = {"info": element, "next": None}
    if my_list['first'] is None:
        my_list['first'] = new_node
        my_list['last'] = new_node
    else:
        new_node['next'] = my_list['first']
        my_list['first'] = new_node
    my_list['size'] += 1
    return my_list
def add_last(my_list, element):
    new_node = {"info": element, "next": None}
    if my_list['first'] is None:
        my_list['first'] = new_node
        my_list['last'] = new_node
    else:
        my_list['last']['next'] = new_node
        my_list['last'] = new_node
    my_list['size'] += 1
    return my_list
def is_empty(my_list):
    if my_list['first'] is None or my_list['last'] is None:
        return True
    else:
        return False
def size(my_list):
    return my_list['size']
def get_element(my_list, pos):
    searchpos = 0
    node = my_list['first']
    while searchpos < pos:
        node = node['next']
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list['first']
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp['next']
            count += 1

    if not is_in_array:
        count = -1
    return count

def first_element(my_list):
    if my_list['first'] is None:
        raise IndexError("list index out of range")
    return my_list['first']['info']

def last_element(my_list):
    if my_list['last'] is None:
        raise IndexError("list index out of range")
    return my_list['last']['info']  

def remove_first(my_list):
    if my_list["size"]==0:
        print("IndexError: list index out of range")
    else:
        nuevo=my_list["first"]
        info=nuevo["info"]
        nuevo=nuevo["next"]
        my_list["first"]=nuevo
        my_list["size"]-=1
        
        return info

def remove_last(my_list):
    if my_list["size"]==0:
        print("IndexError: list index out of range")
    elif my_list["size"]==1:
        info=first_element(my_list)
        my_list=new_list()
        return info
        
    else:
        size=my_list["size"]
        nodo=my_list["first"]
        ultimo=my_list["last"]
        info=ultimo["info"]
        while nodo["next"]!= ultimo:
            nodo=nodo["next"]
        my_list["last"]=nodo
        my_list["last"]["next"]=None
        my_list["size"]-=1
        return info
        
        

def delete_element(my_list,pos):
    if my_list["size"]==0:
        print("IndexError: list index out of range")
    elif pos==0:
        nuevo=my_list["first"]
        nuevo=nuevo["next"]
        my_list["first"]=nuevo
        my_list["size"]-=1
        return my_list
    else:
        size=my_list["size"]
        nodo=my_list["first"]
        primeros=my_list["first"]
        
        for keypos in range(0,pos):
            nodo=nodo["next"]
        ultimos=nodo["next"]
        while primeros["next"]!= nodo:
            primeros=primeros["next"]
        primeros["next"]=ultimos
        my_list["size"]-=1
        return my_list
    
def insert_element(my_list,element,pos):
    if my_list["size"]==0:
        print("IndexError: list index out of range")
    elif pos==0:
        return add_first(my_list,element)
    else:
        size=my_list["size"]
        nodo=my_list["first"]
        primeros=my_list["first"]
        
        for keypos in range(0,pos):
            nodo=nodo["next"]
        while primeros["next"]!= nodo:
            primeros=primeros["next"]
            
        primeros["next"]={"info":element,"next":nodo}
        my_list["size"]+=1
        return my_list


def change_info(my_list,pos,new_info):
    if my_list["size"]==0:
        print("IndexError: list index out of range")
    elif pos==0:
        my_list["first"]["info"]=new_info
        return my_list
    else:
        size=my_list["size"]
        nodo=my_list["first"]
        
        for keypos in range(0,pos):
            nodo=nodo["next"]
        nodo["info"]=new_info
        return my_list
    
def exchange(my_list,pos1,pos2):
    if my_list["size"]==0:
        print("IndexError: list index out of range")
    else:
        val1=get_element(my_list,pos1)
        val2=get_element(my_list,pos2)
        nodo1=my_list["first"]
        nodo2=my_list["first"]
        for keypos in range(0,pos1):
            nodo1=nodo1["next"]
        nodo1["info"]=val2
        for i in range(0,pos2):
            nodo2=nodo2["next"]
        nodo2["info"]=val1
        return my_list

def sub_list(my_list,pos,num_elements):
    if my_list["size"]==0 or num_elements>my_list["size"] or pos>my_list["size"]:
        print("IndexError: list index out of range")
    else:
        nodo=my_list["first"]
        nueva_lista=new_list()
        for keypos in range(0,pos):
            nodo=nodo["next"]
        for i in range(0,num_elements):
            add_last(nueva_lista,nodo["info"])
            nodo=nodo["next"]
        return nueva_lista
def default_sort_criteria(element1,element2):

   is_sorted = False
   if element1 < element2:
      is_sorted = True
   return is_sorted

def insertion_sort(my_list,sort_crit):
    n= my_list["size"]
    
    if sort_crit == True:
        for i in range(1,n):
            key=get_element(my_list,i)
            j=i-1
            while j>=0 and get_element(my_list,j)>key:
                change_info(my_list,j+1,get_element(my_list,j))
                j-=1
            change_info(my_list,j+1,key)
        return my_list
    if sort_crit == True:
        for i in range(1,n):
            key=get_element(my_list,i)
            j=i-1
            while j>=0 and get_element(my_list,j)<key:
                change_info(my_list,j+1,get_element(my_list,j))
                j-=1
            change_info(my_list,j+1,key)
        return my_list
    
def merge(list1,list2, sort_crit):
    resp=new_list()
    tam1=list1["size"]
    tam2=list2["size"]
    if sort_crit==True:
        i=j=0
        while i<tam1 and j<tam2:
            if get_element(list1,i)<=get_element(list2,j):
                add_last(resp,get_element(list1,i))
                i+=1
            else:
                add_last(resp,get_element(list2,j))
                j+=1
        while i<tam1:
            add_last(resp,get_element(list1,i))
            i+=1
        while j<tam2:
            add_last(resp,get_element(list2,j))
            j+=1
        return resp
    else:
        i=j=0
        while i<tam1 and j<tam2:
            if get_element(list1,i)<=get_element(list2,j):
                add_first(resp,get_element(list1,i))
                i+=1
            else:
                add_first(resp,get_element(list2,j))
                j+=1
        while i<tam1 and tam1:
            add_first(resp,get_element(list1,i))
            i+=1
        while j<tam2 and tam2:
            add_first(resp,get_element(list2,j))
            j+=1
        return resp
    
    
    
def merge_sort(my_list,sort_crit):
    def mergear(lista,sort_crit):
        if lista["size"]==1 or lista["size"]==0:
            return lista
        else:
            mid=lista["size"]//2
            izq=mergear(sub_list(lista,0,mid),sort_crit)
            der=mergear(sub_list(lista,mid,lista["size"]-mid),sort_crit)
            resp=merge(izq,der,sort_crit)
            return resp
    resp=mergear(my_list,sort_crit)
    my_list=resp
    return my_list

def quick_sort(my_list, sort_crit):
    low=0
    high=None
    
    if sort_crit==True:
        def quick_sort(my_list,low,high):
            if my_list["size"]==0 or my_list["size"]==1:
                return my_list
            
            if high is None:
                high=my_list["size"]-1
                
            def part(my_list,low,high):
                piv=get_element(my_list,high)
                i=low
                for j in range(low,high):
                    if get_element(my_list,j)<piv:
                        exchange(my_list,i,j)
                        i+=1
                exchange(my_list,i,high)
                return i
            if low<high:
                pivot=part(my_list,low,high)
                quick_sort(my_list,low,pivot-1)
                quick_sort(my_list,pivot+1,high)
            return my_list
        quick_sort(my_list,low,high)
    else:
        def quick_sort(my_list,low,high):
            if my_list["size"]==0 or my_list["size"]==1:
                return my_list
            
            if high is None:
                high=my_list["size"]-1
                
            def part(my_list,low,high):
                piv=get_element(my_list,high)
                i=low
                for j in range(low,high):
                    if get_element(my_list,j)>piv:
                        exchange(my_list,i,j)
                        i+=1
                exchange(my_list,i,high)
                return i
            if low<high:
                pivot=part(my_list,low,high)
                quick_sort(my_list,low,pivot-1)
                quick_sort(my_list,pivot+1,high)
            return my_list
        quick_sort(my_list,low,high)

def selection_sort(my_list,sort_crit):
    size=my_list["size"]
    
    if sort_crit==True:
        for key in range(0,size):
            minimo=key
            for llave in range(key+1,size):
                if get_element(my_list,llave)<get_element(my_list,minimo):
                    minimo=llave
            if minimo!=key:
                exchange(my_list,key,minimo)
        return my_list
    else:
        for key in range(0,size):
            minimo=key
            for llave in range(key+1,size):
                if get_element(my_list,llave)>get_element(my_list,minimo):
                    minimo=llave
            if minimo!=key:
                exchange(my_list,key,minimo)
        return my_list

def shell_sort(my_list,sort_crit):
    
    if sort_crit==True:
        n=my_list["size"]
        h=1
        while h<n//3:
            h=3*h+1
        while h>0:
            for i in range(h,n):
                key=get_element(my_list,i)
                j=i
                while j>=h and get_element(my_list,(j-h))>key:
                    change_info(my_list,j,get_element(my_list,(j-h)))
                    j-=h
                change_info(my_list,j,key)
            h//=3
        return my_list
    else:
        n=my_list["size"]
        h=1
        while h<n//3:
            h=3*h+1
        while h>0:
            for i in range(h,n):
                key=get_element(my_list,i)
                j=i
                while j>=h and get_element(my_list,(j-h))<key:
                    change_info(my_list,j,get_element(my_list,(j-h)))
                    j-=h
                change_info(my_list,j,key)
            h//=3
        return my_list
        
