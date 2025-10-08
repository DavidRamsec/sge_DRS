import math
num = int(input("Introduce el numero que quieres saber si es primo o no: "))
if num <= 1:
    print("No es primo")
elif num == 2:
    print("Es primo")
elif num % 2 == 0:
    print("No es primo")
else:
    es_primo = True
    raiz = int(math.sqrt(num)) + 1
    for i in range(3, raiz, 2):
        compar = num / i
        if compar == int(compar):
            es_primo = False
            break
    if es_primo:
        print("Es primo")
    else:
        print("No es primo")