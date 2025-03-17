def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist

def is_empty(my_list):
    if len(my_list) == 0:
        return True
    else:
        return False
    
def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
            
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    if is_empty(my_list):
        node= {"info": element, "next": None}
        my_list["first"] = node
        my_list["size"] += 1
        my_list["last"] = node
    else:
        node= {"info": element, "next": my_list["first"]}
        my_list["first"] = node
        my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    node= {"info": element, "next": None}
    if is_empty(my_list):
        my_list["first"] = node
        my_list["size"] += 1
        my_list["last"] = node
    else:
        my_list["size"] += 1
        my_list["last"]["next"]= node
        my_list["last"] = node
    return my_list

def last_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        return my_list["last"]["info"]
    
def remove_first(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        my_list["size"] -= 1
    return my_list["first"]["info"]

def remove_last(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        my_list["size"] -= 1
    return my_list["last"]["info"]




def size(new_list):
    return new_list['size'] #retorno el valor que este en size

def first_element(my_list):
    return my_list['first']['info'] # #me paro en el primer elemento, y luego accedo al valor info y lo retorno

def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')

    if pos == 0: # caso de eliminar el primer nodo de la lista
        my_list['first'] = my_list['first']['next'] #cambiar first para que apunte al nodo consecutivo (2ndo nodo)
        if my_list['size'] == 1: # si unicamente el tamaño de la lista era ese unico nodo (1 nodo), ponemos que el apuntador del ultimo valor es nulo (no existe) por lo tanto la lista no tiene mas nodos.
            my_list['last'] = None
    else:
        ant = my_list['first'] #definimos anterior como el primer nodo de la lista
        for i in range(pos - 1): #Recorro la lista hasta posicion -1 veces (El nodo anterior al que me interesa eliminar)
            ant =ant['next']
        ant['next'] = ant['next']['next']# al estar parado en el que deseo eliminar (ant['next']), ahora lo salto usando next para que mi apuntador señale al siguiente del eliminado. 
        if ant['next'] is None: # Si se borro el ultimo nodo de la lista, se acutaliza al nuevo ultimo last. 
            my_list['last']= ant
            
    my_list['size'] -= 1 #actualizar el tamaño de la lista
    return my_list # y listo =)
    
def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    nodo = my_list['first'] #inicio nodo en la primera posicion
    for i in range(pos): #recorro hasta pos
        nodo= nodo['next'] 
    nodo['info'] = new_info #actualizo la informacion
    return my_list #retorno

def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= size(my_list) or pos_2 < 0 or pos_2 >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    nodo1 = my_list['first'] # primera posicion
    for i in range(pos_1): # voy a la posicion n
        nodo1= nodo1['next']
    nodo2 = my_list['first'] 
    for w in range(pos_2):
        nodo2 = nodo2['next']
        
    nodo1['info'], nodo2['info'] = nodo2['info'], nodo1['info'] # intercambio a la vez los dos valores
    return my_list
    
        
def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')

    posicion = my_list['first']
    for z in range(pos):
        posicion = posicion['next']
    x=0
    lista = new_list()
    
    while posicion is not None and x < num_elements:
        add_last(lista, posicion['info'])
        posicion = posicion['next']
        x += 1
    return lista

def insert_element(my_list, element, pos):
    
    if pos < 0 or pos >= size(my_list):
        
        return my_list
    
    nodo_nuevo= {'info':element, 'next': None}
    if pos == 0:
        nodo_nuevo['next']= my_list['first']
    my_list['first'] = nodo_nuevo
    
    if my_list['size'] == 0:
        my_list['last'] = nodo_nuevo
    else:
        anterior = my_list['first']
        for y in range(pos-1):
            anterior = anterior['next']
        
        nodo_nuevo['next'] = anterior['next']
        anterior['next'] = nodo_nuevo

    my_list['size'] +=1
    return my_list
    # final
    
    
    def new_list():
     newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist

def is_empty(my_list):
    
    if my_list["size"] == 0:
        return True
    else:
        return False
    
def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
            
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    
    if is_empty(my_list):
        node= {"info": element, "next": None}
        my_list["first"] = node
        my_list["size"] += 1
        my_list["last"] = node
        
    else:
        node= {"info": element, "next": my_list["first"]}
        my_list["first"] = node
        my_list["size"] += 1
        
    return my_list

def add_last(my_list, element):
    node= {"info": element, "next": None}
    
    if is_empty(my_list):
        my_list["first"] = node
        my_list["size"] += 1
        my_list["last"] = node
    else:
        my_list["size"] += 1
        my_list["last"]["next"]= node
        my_list["last"] = node
    return my_list

def last_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        return my_list["last"]["info"]
    
def remove_first(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        my_list["size"] -= 1
    return my_list["first"]["info"]

def remove_last(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        my_list["size"] -= 1
    return my_list["last"]["info"]

def size(new_list):
    return new_list['size'] #retorno el valor que este en size

def first_element(my_list):
    return my_list['first']['info'] # #me paro en el primer elemento, y luego accedo al valor info y lo retorno

def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')

    if pos == 0: # caso de eliminar el primer nodo de la lista
        my_list['first'] = my_list['first']['next'] #cambiar first para que apunte al nodo consecutivo (2ndo nodo)
        if my_list['size'] == 1: # si unicamente el tamaño de la lista era ese unico nodo (1 nodo), ponemos que el apuntador del ultimo valor es nulo (no existe) por lo tanto la lista no tiene mas nodos.
            my_list['last'] = None
    else:
        ant = my_list['first'] #definimos anterior como el primer nodo de la lista
        for i in range(pos - 1): #Recorro la lista hasta posicion -1 veces (El nodo anterior al que me interesa eliminar)
            ant =ant['next']
        ant['next'] = ant['next']['next']# al estar parado en el que deseo eliminar (ant['next']), ahora lo salto usando next para que mi apuntador señale al siguiente del eliminado. 
        if ant['next'] is None: # Si se borro el ultimo nodo de la lista, se acutaliza al nuevo ultimo last. 
            my_list['last']= ant
            
    my_list['size'] -= 1 #actualizar el tamaño de la lista
    return my_list # y listo =)
    
def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    nodo = my_list['first'] #inicio nodo en la primera posicion
    for i in range(pos): #recorro hasta pos
        nodo= nodo['next'] 
    nodo['info'] = new_info #actualizo la informacion
    return my_list #retorno

def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= size(my_list) or pos_2 < 0 or pos_2 >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    nodo1 = my_list['first'] # primera posicion
    for i in range(pos_1): # voy a la posicion n
        nodo1= nodo1['next']
    nodo2 = my_list['first'] 
    for w in range(pos_2):
        nodo2 = nodo2['next']
        
    nodo1['info'], nodo2['info'] = nodo2['info'], nodo1['info'] # intercambio a la vez los dos valores
    return my_list
    
        
def sub_list(my_list, pos, num_elements):
    
    if pos < 0 or pos >= size(my_list):
        
        raise Exception('IndexError: list index out of range')

    posicion = my_list['first']
    for z in range(pos):
        posicion = posicion['next']
    x=0
    lista = new_list()
    
    while posicion is not None and x < num_elements:
        add_last(lista, posicion['info'])
        posicion = posicion['next']
        x += 1
    return lista


def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
            
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    if is_empty(my_list):
        node= {"info": element, "next": None}
        my_list["first"] = node
        my_list["size"] += 1
        my_list["last"] = node
    else:
        node= {"info": element, "next": my_list["first"]}
        my_list["first"] = node
        my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    node= {"info": element, "next": None}
    if is_empty(my_list):
        my_list["first"] = node
        my_list["size"] += 1
        my_list["last"] = node
    else:
        my_list["size"] += 1
        my_list["last"]["next"]= node
        my_list["last"] = node
        
    return my_list

def last_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        return my_list["last"]["info"]
    
def remove_first(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        my_list["size"] -= 1
    return my_list["first"]["info"]

def remove_last(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        my_list["size"] -= 1
    return my_list["last"]["info"]



def default_sort_criteria (element_1, element_2):
    is_sorted = False
    
    if element_1 < element_2:
        is_sorted = True 
    
    return is_sorted



def quick_sort(list, sort_crit = default_sort_criteria):
    
    def iter_quick(list, inf, sup):
        
        if sup <= inf:
            
            return list
            
        else: 
                 
            pbot = divi(list, inf, sup)
            
            iter_quick(list, inf, pbot - 1)
            iter_quick(list, pbot + 1, sup)
        
        return list
    
    return iter_quick(list, 0, size(list) - 1)
            
            

def divi(list, inf, sup):
    
    pbot = get_element(list, sup)
    
    i = inf - 1
    
    for j in range(inf, sup):
        
        if get_element(list, j) < pbot:
            
            i += 1
            
            list = exchange(list, i, j)
            
    i += 1 
    list = exchange(list, i, sup)
    
    return i
            
       
def insertion_sort(list, sort_crit = default_sort_criteria):
    
    for i in range(1, size(list)):
        
        ver = get_element(list, i)
        
        j = i -1
        
        while j >= 0 and get_element(list, j)["average_rating"] > ver["average_rating"]:
            
            list = change_info(list, j + 1, get_element(list, j))
            j -= 1
            
        list = change_info(list, j + 1, ver)

    return list
     


def shell_sort (my_list, sort_crit = default_sort_criteria):
    size = my_list["size"]
    
    if size < 2:
        return my_list
    
    elements = []
    current = my_list["first"]
    
    while current != None:
        elements.append(current)
        current = current["next"]
        
    h = 1
    
    while h < size:
        h = 3 * h + 1
        
    while h > 0:
        h = h // 3
        
        for i in range(h, size):
            j = i
            
            while j >= h and sort_crit(elements[j].value, elements[j-h].value):
                elements[j].value = elements[j-h].value
                elements[j-h].value = elements[j].value
                j -= h
                          
    return my_list


def split(my_list):
    
    if my_list['size'] <= 1:
        
        return my_list, {'size': 0, 'first': None}
    
    mid = my_list['size'] // 2
    
    actual = my_list['first']
    
    previo = None
    
    for x in range(mid):
        
        previo = actual
        
        actual = actual['next']
    
    if previo:
        
        previo['next'] = None  

    mitad_izquierda = {'size': mid, 'first': my_list['first']}
    
    mitad_derecha = {'size': my_list['size'] - mid, 'first': actual}
    
    return mitad_izquierda, mitad_derecha


def merge(mitad_izquierda, mitad_derecha, sort_crit=default_sort_criteria):
    
    i = mitad_izquierda['first']
    d = mitad_derecha['first']
    
    if not i:
        
        return mitad_derecha
    
    if not d:
        return mitad_izquierda
    
    
    if sort_crit(i['info'], d['info']):
        
        resultado = merge({'size': 0, 'first': i['next']}, mitad_derecha, sort_crit)
        
        i['next'] = resultado['first']
    
        return {'size': mitad_izquierda['size'] + mitad_derecha['size'], 'first': i}
    
    else:
        
        resultado = merge(mitad_izquierda, {'size': 0, 'first': d['next']}, sort_crit)
        
        d['next'] = resultado['first']
        
        return  {'size': mitad_izquierda['size'] + mitad_derecha['size'], 'first': d}


def merge_sort(my_list, sort_crit=default_sort_criteria):
    
    if my_list['size'] <= 1:
        
        return my_list  

    mitad_izquierda, mitad_derecha = split(my_list)


    
    izquierda_ordenada = merge_sort(mitad_izquierda, sort_crit)
    
    derecha_ordenada = merge_sort(mitad_derecha, sort_crit)

    result = merge(izquierda_ordenada, derecha_ordenada, sort_crit)
    
    lista_ordenada = {'size': result['size'], 'first': result['first']}

    return lista_ordenada


def selection_sort(my_list, sort_crit=default_sort_criteria):

    if my_list['size'] <= 1 or not my_list['first']:
    
        return my_list 

    values = []
    actual = my_list['first']
    
    while actual:
        values.append(actual['info'])
        actual = actual['next']

    n = len(values)
    
    
    for i in range(n):
        indx_menor = i
        for j in range(i + 1, n):
            if sort_crit(values[j], values[indx_menor]):
                indx_menor = j
        values[i], values[indx_menor] = values[indx_menor], values[i]

    actual = my_list['first']
    for value in values:
        
        actual['info'] = value 
        
        actual = actual['next']

    return my_list

    


        
    