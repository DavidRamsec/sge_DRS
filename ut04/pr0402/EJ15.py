cadena = input("Escribe una frase: ")
cadenaC = input("Escribe la frase que quieres comparar: ")
cUno = 0
cDos = 0
for c in cadena:
    cUno += ord(c)
for c in cadenaC:
    cDos += ord(c)
if cUno > cDos:
    print("La primera frase tiene un mayor valor ASCII")
else:
    print("La segunda frase tiene un mayor valor ASCII")