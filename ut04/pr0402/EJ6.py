cadena = input("Escribe una frase: ")
res = ""
for c in cadena:
    if c.islower():
        c = c.capitalize()
    else:
        c = c.lower()
    res = res+c
print(res)