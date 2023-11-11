""" 
    vaciar la lista
    [100,200,300,400,500,600,700]  result >  [] 
"""

array = [100,200,300,400,500,600,700]

def hack(array: list):
    array.clear()
    return array

print(hack(array))