cadena = input("Escribe una frase: ").title()
res = ""
i = 0;
for c in cadena:
    if c.isalnum():
        if i == 0:
            res += c.lower()
        else:
            res += c
        i += 1
print(res)