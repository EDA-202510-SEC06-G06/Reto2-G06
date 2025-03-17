import array_list as lt

def new_queue():
    return lt.new_list()

def enqueue(my_queue, element):
    return lt.add_first(my_queue, element)

def peek(my_queue):
    
    return lt.get_element(my_queue, my_queue["size"] - 1)

def size(my_queue):
    
    return my_queue["size"]

def is_empty(my_queue):
    
    return my_queue["size"] == 0

def dequeue(my_queue):
    
    if is_empty(my_queue):
        
        return "EmptyStructureError: queue is empty"
    
    else:
        
        return lt.remove_last(my_queue)

    

