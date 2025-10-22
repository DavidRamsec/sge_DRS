palabras = ["hola","buenas","cangrejo","hola"]
palabra = input("Escribe una palabra: ")
i = 0
for p in palabras:
    if p == palabra:
        i += 1
print("Tu palabra aparece ",i," veces")
