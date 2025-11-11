numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def filtrar_pares(numero):
    return numero % 2 == 0
res = list(filter(filtrar_pares, numeros))
print(res)
