def new_list():
    newlist={
        "elements": [],
        "size": 0,
        
    }
    return newlist
def get_element(my_list, index):
    if index < 0 or index >= my_list["size"]:
        raise IndexError("Index out of range")
    return my_list["elements"][index]

def is_present (my_list, element,cmp_function):
    size=my_list["size"]

    if size>0:
        keyexist=False
        for keypos in range(0,size):
            info=my_list["elements"][keypos]
            if cmp_function(element,info)==0:
                keyexist=True
                break
            if keyexist:
                return keypos
    return -1

def add_first(my_list,element):
    if my_list["size"] == 0:
        my_list["elements"].append(element)
        my_list["size"]+=1
    else:
        size=my_list["size"]
        my_list["size"]+=1

        if size==0:
            my_list["elements"].append(element)
        else:
            aux=my_list["elements"]
            aux=reversed(aux)
            aux.append(element)
            my_list["elements"]=reversed(aux)
    return my_list
def remove_first(my_list):
    if my_list["size"] == 0:
        return None
    first_element = my_list["elements"].pop(0)
    my_list["size"] -= 1
    return first_element
def remove_last(my_list):
    if my_list["size"] == 0:
        return None
    last_element = my_list["elements"].pop(-1)
    my_list["size"] -= 1
    return last_element
def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list["size"]:
        raise IndexError("Index out of range")
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list
def delete_element(my_list, element):
    if element in my_list["elements"]:
        my_list["elements"].remove(element)
        my_list["size"] -= 1
    return my_list
def change_info(my_list, index, new_element):
    if 0 <= index < my_list["size"]:
        my_list["elements"][index] = new_element
    return my_list
def exchange(my_list, index1, index2):
    if 0 <= index1 < my_list["size"] and 0 <= index2 < my_list["size"]:
        my_list["elements"][index1], my_list["elements"][index2] = my_list["elements"][index2], my_list["elements"][index1]
    return my_list
def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= my_list["size"]:
        raise IndexError("list index out of range")
    if num_elements < 0:
        raise ValueError("num_elements must be non-negative")
    if pos_i + num_elements > my_list["size"]:
        raise IndexError("list index out of range")

    sub_elements = my_list["elements"][pos_i:pos_i + num_elements]
    return {
        "size": len(sub_elements),
        "elements": sub_elements
    }
    
def add_last (my_list,element):
    my_list["elements"].append(element)
    my_list["size"]+=1
    return my_list

def is_empty(my_list):
    if my_list["size"]<=0:
        return True
    else:
        return False
    
def size(my_list):
    return my_list["size"]

def first_element(my_list):
    first=my_list["elements"][0]
    return first

def last_element(my_list):
    size=my_list["size"]
    last=my_list["elements"][size-1]
    return last

def default_sort_criteria(element1,element2):

   is_sorted = False
   if element1 < element2:
      is_sorted = True
   return is_sorted

def insertion_sort(my_list,sort_crit):
    n= my_list["size"]
    
    if sort_crit == True:
        for i in range(1,n):
            key=my_list["elements"][i]
            j=i-1
            while j>=0 and my_list["elements"][j]>key:
                change_info(my_list,j+1,get_element(my_list,j))
                j-=1
            change_info(my_list,j+1,key)
        return my_list
    else:
        for i in range(1,n):
            key=my_list["elements"][i]
            j=i-1
            while j>=0 and my_list["elements"][j]<key:
                change_info(my_list,j+1,get_element(my_list,j))
                j-=1
            change_info(my_list,j+1,key)
        return my_list
    
def merge(list1,list2, sort_crit):
    
    if sort_crit==True:
        i=j=0
        resp=[]
        while i<len(list1) and j<len(list2):
            if list1[i]<=list2[j]:
                resp.append(list1[i])
                i+=1
            else:
                resp.append(list2[j])
                j+=1
        while i<len(list1):
            resp.append(list1[i])
            i+=1
        while j<len(list2):
            resp.append(list2[j])
            j+=1
        return resp
    else:
        i=j=0
        resp=[]
        while i<len(list1) and j<len(list2):
            if list1[i]>=list2[j]:
                resp.append(list1[i])
                i+=1
            else:
                resp.append(list2[j])
                j+=1
        while i<len(list1):
            resp.append(list1[i])
            i+=1
        while j<len(list2):
            resp.append(list2[j])
            j+=1
        return resp
    
    
    
def merge_sort(my_list,sort_crit):
    lista=my_list["elements"]
    def mergear(lista,sort_crit):
        if len(lista)==1 or len(lista)==0:
            return lista
        else:
            mid=len(lista)//2
            izq=mergear(lista[:mid],sort_crit)
            der=mergear(lista[mid:],sort_crit)
            resp=merge(izq,der,sort_crit)
            return resp
    resp=mergear(lista,sort_crit)
    my_list["elements"]=resp
    return my_list

def merge_especializado(list1,list2, sort_crit,llave,llave2):
    
    if sort_crit==True:
        i=j=0
        resp=[]
        while i<len(list1) and j<len(list2):
            if list1[i][llave]<list2[j][llave]:
                resp.append(list1[i])
                i+=1
            elif list1[i][llave]==list2[j][llave]:
                if list1[i][llave2]<=list2[j][llave2]:
                    resp.append(list1[i])
                    i += 1
                else:
                    resp.append(list2[j])
                    j += 1
            else:
                resp.append(list2[j])
                j+=1
        while i<len(list1):
            resp.append(list1[i])
            i+=1
        while j<len(list2):
            resp.append(list2[j])
            j+=1
        return resp
    else:
        i=j=0
        resp=[]
        while i<len(list1) and j<len(list2):
            if list1[i][llave]>=list2[j][llave]:
                resp.append(list1[i])
                i+=1
            elif list1[i][llave]==list2[j][llave]:
                if list1[i][llave2]>list2[j][llave2]:
                    resp.append(list1[i])
                    i += 1
                elif list1[i][llave]==list2[j][llave]:
                    if list1[i][llave2]<=list2[j][llave2]:
                        resp.append(list1[i])
                        i += 1
                else:
                    resp.append(list2[j])
                    j += 1
            else:
                resp.append(list2[j])
                j+=1
        while i<len(list1):
            resp.append(list1[i])
            i+=1
        while j<len(list2):
            resp.append(list2[j])
            j+=1
        return resp
    
def merge_especializado2(list1,list2, sort_crit,llave,llave2,llave3, llave4):
    
    if sort_crit==True:
        i=j=0
        resp=[]
        while i<len(list1) and j<len(list2):
            if list1[i][llave]<list2[j][llave]:
                resp.append(list1[i])
                i+=1
            elif list1[i][llave]==list2[j][llave]:
                if list1[i][llave2]<=list2[j][llave2]:
                    resp.append(list1[i])
                    i += 1
                    
                elif list1[i][llave2]==list2[j][llave2]:
                    if list1[i][llave3]<list2[j][llave3]:
                        resp.append(list1[i])
                        i += 1
                elif list1[i][llave3]==list2[j][llave3]:
                    if list1[i][llave4]<=list2[j][llave4]:
                        resp.append(list1[i])
                        i += 1
                else:
                    resp.append(list2[j])
                    j += 1
            else:
                resp.append(list2[j])
                j+=1
        while i<len(list1):
            resp.append(list1[i])
            i+=1
        while j<len(list2):
            resp.append(list2[j])
            j+=1
        return resp

    else:
        i=j=0
        resp=[]
        while i<len(list1) and j<len(list2):
            if list1[i][llave]>=list2[j][llave]:
                resp.append(list1[i])
                i+=1
            elif list1[i][llave]==list2[j][llave]:
                if list1[i][llave2]>=list2[j][llave2]:
                    resp.append(list1[i])
                    i += 1
                elif list1[i][llave2]==list2[j][llave2]:
                    if list1[i][llave3]>list2[j][llave3]:
                        resp.append(list1[i])
                        i += 1
                elif list1[i][llave3]==list2[j][llave3]:
                    if list1[i][llave4] >=list2[j][llave4]:
                        resp.append(list1[i])
                        i += 1
                else:
                    resp.append(list2[j])
                    j += 1
            else:
                resp.append(list2[j])
                j+=1
        while i<len(list1):
            resp.append(list1[i])
            i+=1
        while j<len(list2):
            resp.append(list2[j])
            j+=1
        return resp

def merge_sort_especializado(my_list,sort_crit,llave1,llave2):
    lista=my_list["elements"]
    def mergear(lista,sort_crit):
        if len(lista)==1 or len(lista)==0:
            return lista
        else:
            mid=len(lista)//2
            izq=mergear(lista[:mid],sort_crit)
            der=mergear(lista[mid:],sort_crit)
            resp=merge_especializado(izq,der,sort_crit,llave1,llave2)
            return resp
    resp=mergear(lista,sort_crit)
    my_list["elements"]=resp
    return my_list
    
def merge_sort_especializado2(my_list,sort_crit,llave1,llave2,llave3,llave4):
    lista=my_list["elements"]
    def mergear(lista,sort_crit):
        if len(lista)==1 or len(lista)==0:
            return lista
        else:
            mid=len(lista)//2
            izq=mergear(lista[:mid],sort_crit)
            der=mergear(lista[mid:],sort_crit)
            resp=merge_especializado2(izq,der,sort_crit,llave1,llave2,llave3,llave4)
            return resp
    resp=mergear(lista,sort_crit)
    my_list["elements"]=resp    
    return my_list

def quick_sort(my_list, sort_crit):
    low=0
    high=None
    
    if sort_crit==True:
        def quick_sort(my_list,low,high):
            if my_list["size"]==0 or my_list["size"]==1:
                return my_list
            
            if high is None:
                high=len(my_list["elements"])-1
                
            def part(my_list,low,high):
                piv=my_list["elements"][high]
                i=low
                for j in range(low,high):
                    if my_list["elements"][j]<piv:
                        my_list["elements"][i], my_list["elements"][j] = my_list["elements"][j], my_list["elements"][i]
                        i+=1
                my_list["elements"][i], my_list["elements"][high] = my_list["elements"][high], my_list["elements"][i]
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
                high=len(my_list["elements"])-1
                
            def part(my_list,low,high):
                piv=my_list["elements"][high]
                i=low
                for j in range(low,high):
                    if my_list["elements"][j]>piv:
                        my_list["elements"][i], my_list["elements"][j] = my_list["elements"][j], my_list["elements"][i]
                        i+=1
                my_list["elements"][i], my_list["elements"][high] = my_list["elements"][high], my_list["elements"][i]
                return i
            if low<high:
                pivot=part(my_list,low,high)
                quick_sort(my_list,low,pivot-1)
                quick_sort(my_list,pivot+1,high)
            return my_list
def merge_sort_accidentes(lista):
    """
    Ordena una lista de accidentes usando Merge Sort
    con el criterio de Start_Lat, Start_Lng, End_Lat, End_Lng
    """
    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2
    izquierda = merge_sort_accidentes(lista[:mitad])
    derecha = merge_sort_accidentes(lista[mitad:])

    return merge_accidentes(izquierda, derecha)

def merge_accidentes(izquierda, derecha):
    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        comparacion = comparar_accidentes(izquierda[i], derecha[j])
        if comparacion == -1:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

def selection_sort(my_list,sort_crit):
    size=my_list["size"]
    
    if sort_crit==True:
        for key in range(0,size):
            minimo=key
            for llave in range(key+1,size):
                if my_list["elements"][llave]<my_list["elements"][minimo]:
                    minimo=llave
            if minimo!=key:
                exchange(my_list,key,minimo)
        return my_list
    else:
        for key in range(0,size):
            minimo=key
            for llave in range(key+1,size):
                if my_list["elements"][llave]>my_list["elements"][minimo]:
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
                key=my_list["elements"][i]
                j=i
                while j>=h and my_list["elements"][j-h]>key:
                    my_list["elements"][j]=my_list["elements"][j-h]
                    j-=h
                my_list["elements"][j]=key
            h//=3
        return my_list
    else:
        n=my_list["size"]
        h=1
        while h<n//3:
            h=3*h+1
        while h>0:
            for i in range(h,n):
                key=my_list["elements"][i]
                j=i
                while j>=h and my_list["elements"][j-h]<key:
                    my_list["elements"][j]=my_list["elements"][j-h]
                    j-=h
                my_list["elements"][j]=key
            h//=3
        return my_list
