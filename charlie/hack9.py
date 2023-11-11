""" 
    agregar tú alias al inicio
    [100,200,300,400,500,600,700]  result >  [foo,100,200,300,400,500,600,700]
"""
array = [100,200,300,400,500,600,700]

def hack(array: list):
    array.insert(0, 'charlie')
    return array

print(hack(array))