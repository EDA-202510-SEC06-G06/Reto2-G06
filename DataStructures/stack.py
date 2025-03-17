import array_list as arr

def new_stack():
    
    return arr.new_list()

def is_empty(stack):
    
    return arr.is_empty(stack)

def size(stack):
    
    return arr.size(stack)

def push(stack, element):
    
    if element is None:
        
        return None
        
    else:
        arr.add_last(stack, element)
        return stack

def pop(stack):
    if is_empty(stack):
        return None
    
    return arr.remove_last(stack)

def top(stack):
    if is_empty(stack):
        return None
    
    return arr.get_element(stack, arr.size(stack) - 1)

