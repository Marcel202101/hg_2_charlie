""" 
    agregar después del item 500
    los alias qux y thud
    [100,200,300,400,500,600,700]  result >  [100,200,300,400,500,qux,thud,600,700]
"""

array = [100,200,300,400,500,600,700]

def hack(array: list):
    array.insert(array.index(600), 'qux')
    array.insert(array.index(600), 'thud')
    return array

print(hack(array))