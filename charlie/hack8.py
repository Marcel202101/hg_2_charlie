""" 
    agregar tú alias al final
    [100,200,300,400,500,600,700]  result >  [100,200,300,400,500,600,700,foo]
"""

array = [100,200,300,400,500,600,700]

def hack(array: list):
    array.append('charlie')
    return array

print(hack(array))