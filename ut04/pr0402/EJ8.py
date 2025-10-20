cadena = input("Escribe una frase: ").replace(" ", "").lower()
cadenaD = input("Escribe la frase con la que quieres comparar: ").replace(" ", "").lower()
if sorted(cadena) == sorted(cadenaD):
    print("Son anagramas")
else:
    print("No son anagramas")

