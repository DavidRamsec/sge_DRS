num = str(input("Introduce cinco números: "))
numeros = num.split(" ")
numeros = [int(n) for n in numeros]
may = numeros[0]
men = numeros[0]
for i in range(len(numeros)):
    if(numeros[i]>may):
        may = numeros[i]
    if(numeros[i]<men):
        men = numeros[i]
print("el mayor es: ",may,"y el menor es: ",men)