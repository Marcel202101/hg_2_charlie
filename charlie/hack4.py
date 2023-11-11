""" 
    eliminar los items 300 y 500
    [100,200,300,400,500,600,700]  result >  [100,200,400,600,700]
"""

array = [100,200,300,400,500,600,700]

def hack(array: list):
    array.pop(array.index(300))
    array.pop(array.index(500))
    return array

print(hack(array))