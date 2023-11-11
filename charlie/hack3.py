""" 
    eliminar el último item
    [100,200,300,400,500,600,700]  result >  [100,200,300,400,500,600]
"""

array = [100,200,300,400,500,600,700]

def hack(array: list):
    array.pop()
    return array

print(hack(array))