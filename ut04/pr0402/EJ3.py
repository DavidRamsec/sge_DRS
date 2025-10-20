cadena = input("Escribe una frase: ")
letras = []
res = ""
for c in cadena:
    letras.append(c)
i = len(letras)-1
while i >= 0:
    res = res+letras[i]
    i = i-1
if cadena == res:
    print("Es un palíndromo")
else:
    print("No es palíndromo")
print(res)