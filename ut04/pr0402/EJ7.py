cadena = input("Escribe una frase: ")
numero = int(input("Escribe un numero: "))
res = ""
almac = cadena[-numero:]
cadena = cadena[:-numero]
res = almac + cadena
print(res)