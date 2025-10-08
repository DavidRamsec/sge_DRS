num = float(input("Introduce el valor: "))
medida = str(input("Introduce la unidad de medida: "))
conver = str(input("Introduce la medida a la que quieres convertir: "))
if(medida == "mm" and conver == "cm"):
    num = num / 10
if(medida == "mm" and conver == "m"):
    num = num / 1000
if(medida == "mm" and conver == "km"):
    num = num / 1000000
if(medida == "cm" and conver == "mm"):
    num = num * 10
if(medida == "cm" and conver == "m"):
    num = num / 100
if(medida == "cm" and conver == "km"):
    num = num / 100000
if(medida == "m" and conver == "mm"):
    num = num * 1000
if(medida == "m" and conver == "cm"):
    num = num * 100
if(medida == "m" and conver == "km"):
    num = num / 1000
if(medida == "km" and conver == "mm"):
    num = num * 1000000
if(medida == "km" and conver == "cm"):
    num = num * 100000
if(medida == "km" and conver == "m"):
    num = num * 1000
print(num,conver)