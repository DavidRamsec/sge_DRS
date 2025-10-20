cadena = input("Escribe una frase: ")
res = ""
for c in cadena:
    if c.isalnum() or c == " ":
        res += c
print(res)