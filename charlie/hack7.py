""" 
    remplazar el item 300 
    por tú alias
    [100,200,300,400,500,600,700]  result >  [100,200,foo,400,500,600,700]
"""

array = [100,200,300,400,500,600,700]

def hack(array: list):
    array[array.index(300)] = 'charlie'
    return array

print(hack(array))