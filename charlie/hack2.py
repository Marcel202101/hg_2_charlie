""" 
    eliminar el primer item
    [100,200,300,400,500,600,700]  result >  [200,300,400,500,600,700]
"""

array = [100,200,300,400,500,600,700]

def hack(array: list):
    array.pop(0)
    return array

print(hack(array))