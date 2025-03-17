def new_list():
    
    array = {"size": 0, "elements" :[]}
    
    return array
   
    
def get_element(my_list, index):
    
    if index > size(my_list) or index < 0:
        
        return "IndexError: list index out of range"
    
    else:
        
        return my_list["elements"][index]


def is_present(my_list,  element, cmp_function):
    
    size = my_list["size"]
    
    if size > 0:
        
        keyexist = False
        
        for keypos in range(0, size):
            
            info = my_list["elements"][keypos]
            
            if cmp_function(element, info) == 0:
                
                keyexist = True
                
                break 
            
        if keyexist:
            
            return keypos

    return -1


def add_first(my_list, element):
    
    my_list["elements"].insert(0, element)
    
    my_list["size"] += 1
    
    return my_list


def add_last(my_list, element):
    
    my_list["elements"].append(element)
    
    my_list["size"] += 1
    
    return my_list


def size(my_list):
    
    return my_list["size"]


def first_element(my_list):
    
    if size(my_list) == 0:
        
        return "IndexError: list index out of range"
    
    else:
        
        return my_list["elements"][size(my_list) - 1]
    

def is_empty(my_list):
    
    if my_list["size"] == 0:
        
        return True
    
    else:
        
        return  False
      

def remove_first(my_list):
    
    if is_empty(my_list):
        
        return "IndexError: list index out of range"
    
    else:
        
        my_list["size"] -= 1
        return my_list["elements"].pop(0)
    

def remove_last(my_list):
    
    if is_empty(my_list):
        
        return "IndexError: list index out of range"
    
    else:
        
        my_list["size"] -= 1
        return my_list["elements"].pop(my_list["size"])
    
    
def insert_element(my_list, element, pos):
    
    my_list["elements"].insert(pos, element)
    
    return my_list


def sub_list(my_list, pos_i, num_elements):
    
    if my_list["size"] < pos_i:
        
        return "IndexError: list index out of range"
    
    else:
        #Esta debería ser la manera correcta, Sí pide una lista 
        """"
        new_list = my_list["elements"][pos_i : (pos_i + num_elements)]
        return new_list
        """
        
        #Si lo que realemnte pide es una lista hecha (dict) sería así:
        #Y de hecho esto es lo que funciona
        my_list["elements"] = my_list["elements"][pos_i : (pos_i + num_elements)]
        my_list["size"] = num_elements
        return my_list
    

def delete_element(my_list, pos):
    
    if not 0 <= pos < size(my_list):
        
        return "IndexError: list index out of range"
    
    else:
        
        my_list["elements"].pop(pos)
        my_list["size"] -= 1
        return my_list
    

def change_info(my_list, pos, new_info):
    
    if my_list["size"] < pos:
        
        return "IndexError: list index out of range"
    
    else:
        
        my_list["elements"][pos] = new_info
        return my_list
    

def exchange(my_list, pos_1, pos_2):
    
    if my_list["size"] < pos_2 or my_list["size"] < pos_1:
        
        return "IndexError: list index out of range"
    
    else:
        
        temp = my_list["elements"][pos_1]
        my_list["elements"][pos_1] = my_list["elements"][pos_2]
        my_list["elements"][pos_2] = temp
        return my_list
    
    
def default_sort_criteria (element_1, element_2):
    is_sorted = False
    
    if element_1 < element_2:
        is_sorted = True 
    
    return is_sorted


def shell_sort (my_list, sort_crit = default_sort_criteria):
    size = my_list["size"]
    elements = my_list["elements"]
    
    if size < 2:
        return my_list
    
    h = 1
    
    while h < size:
        h = 3 * h + 1
        
    while h > 0:
        h = h // 3
        
        for i in range(h, size):
            j = i
            
            while j >= h and sort_crit(elements[j], elements[j-h]):
                elements[j] = elements[j-h]
                elements[j-h] = elements[j]
                j -= h
                          
    return my_list




def insertion_sort(array, sort_crit = default_sort_criteria):
    
    for i in range(1, size(array)):
        
        ver = get_element(array, i)
        
        j = i -1
        
        while j >= 0 and get_element(array, j)["average_rating"] > ver["average_rating"]:
            
            array = change_info(array, j + 1, get_element(array, j))
            j -= 1
            
        array = change_info(array, j + 1, ver)

    return array


def quick_sort(array, sort_crit = default_sort_criteria):
    
    def iter_quick(array, inf, sup):
        
        if sup <= inf:
            
            return array
            
        else: 
                 
            pbot = divi(array, inf, sup)
            
            iter_quick(array, inf, pbot - 1)
            iter_quick(array, pbot + 1, sup)
        
        return array
    
    return iter_quick(array, 0, size(array) - 1)
            
            

def divi(array, inf, sup):
    
    pbot = get_element(array, sup)
    
    i = inf - 1
    
    for j in range(inf, sup):
        
        if get_element(array, j) < pbot:
            
            i += 1
            
            array = exchange(array, i, j)
            
    i += 1 
    array = exchange(array, i, sup)
    
    return i


def split(lst):

    if len(lst) <= 1:
        return lst, []
    medio = len(lst) // 2
    return lst[:medio], lst[medio:]

def merge(lst1, lst2, sort_crit=default_sort_criteria):

    lst = []
    
    while lst1 and lst2:
        if sort_crit(lst1[0], lst2[0]):
            lst.append(lst1.pop(0))
        else:
            lst.append(lst2.pop(0))
    
    return lst + lst1 + lst2

def merge_sort(my_list, sort_crit=default_sort_criteria):

    if my_list["size"] <= 1:
        return my_list
    
    lst = my_list["elements"]
    left, right = split(lst)
    
    left_sorted = merge_sort({"size": len(left), "elements": left}, sort_crit)
    right_sorted = merge_sort({"size": len(right), "elements": right}, sort_crit)
    
    sorted_elements = merge(left_sorted["elements"], right_sorted["elements"], sort_crit)
    
    return {"size": len(sorted_elements), "elements": sorted_elements}


def selection_sort(my_list, sort_crit=default_sort_criteria):
    
    size = my_list["size"]
    elements = my_list["elements"]
    
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if sort_crit(elements[j], elements[min_index]):
                min_index = j

        elements[i], elements[min_index] = elements[min_index], elements[i]
    
    return my_list