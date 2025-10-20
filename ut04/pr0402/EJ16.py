cadena = input("Escribe una frase: ")
lista = cadena.split()
i = 0
for c in lista:
    if len(c) > i:
        i = len(c)

print("La longitud de la palabra más larga es: ", i)