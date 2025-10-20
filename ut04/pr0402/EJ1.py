cadena = input("Escribe una frase: ")
voc = 0
con = len(cadena)
vocales = ["a","e","i","o","u"]
for c in cadena:
    if c in vocales:
        voc = voc + 1
    else:
        con = con - 1
print("Hay ",voc," vocales y ",con," consonantes")