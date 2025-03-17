import DataStructures.List.array_list as arr
from DataStructures.Utils import error as err

def new_stack():
    
    return arr.new_list()

def is_empty(stack):
    
    return arr.is_empty(stack)

def size(stack):
    
    return arr.size(stack)

def push(stack, element):
    
    if element is None:
        
        err.error("Element is None")
    else:
        arr.add_last(stack, element)
        return stack

def pop(stack):
    if is_empty(stack):
        err.error("Stack is empty")
        return None
    
    return arr.remove_last(stack)

def top(stack):
    if is_empty(stack):
        err.error("Stack is empty")
        return None
    
    return arr.get_element(stack, arr.size(stack) - 1)


stack = new_stack()

stack = push(stack, 3)
stack = push(stack, 2)
stack = push(stack, 3)
stack = push(stack, 4)
stack = push(stack, 5)

print(stack)
