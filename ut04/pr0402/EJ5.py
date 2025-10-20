cadena = input("Escribe una frase: ")
letras = []
res = ""
for c in cadena:
    if c not in letras:
        letras.append(c)
        res = res+c
        res
print(res)