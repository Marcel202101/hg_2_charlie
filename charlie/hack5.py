""" 
    clonar lista
    [100,200,300,400,500,600,700]  result >  [100,200,300,400,500,600,700]
"""

array = [100,200,300,400,500,600,700]

def hack(array: list):
    return array.copy()

print(hack(array))