numeros = [1,2,3,4,21,76,-12,54,0,67,45]
max = numeros[1]
min = numeros[1]
for n in numeros:
    if n > max:
        max = n
    if n < min:
        min = n
print("maximo: ",max)
print("minimo: ",min)