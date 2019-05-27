# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script

def countwords(lst:list): 
    items = {}
    for i in lst: 
        if i in items.keys(): 
            items[i] += 1
        else:
            items[i] = 1
    return(items) 
    

