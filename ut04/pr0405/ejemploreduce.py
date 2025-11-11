from functools import reduce

numeros =  [1, 2, 3, 4, 5, 6]

def multiplica(num, acum):
    return num*acum

pares = filter(lambda num: num%2 == 0, numeros)

mult = reduce(multiplica, pares, 1)
print(mult)
