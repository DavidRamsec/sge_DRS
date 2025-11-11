numeros1 = [1, 2, 5, 6, 7, 3, 9]
numeros2 = [1, 5, 8, 4, 7]
def ambas(numero):
    return numero in numeros2
res = list(filter(ambas, numeros1))
print(res)