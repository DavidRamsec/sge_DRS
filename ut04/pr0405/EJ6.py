from functools import reduce

numeros = [[-3, 2. 7], [10. -5, 3], [0, 8, -2]]

def func ( acum, item):
    return acum + item

lista = reduce(lambda acum, item: acum + item, numeros, [])
print(lista)