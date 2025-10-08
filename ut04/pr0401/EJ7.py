from random import *
num = randint(0, 100)
entrada = int(input("Escribe un numero del 0 al 100: "))
while(entrada != num):
    if (entrada > num):
        entrada = int(input("Demasiado alto, prueba otra vez: "))
    if (entrada < num):
        entrada = int(input("demasiado bajo, prueba otra vez: "))
print("Correcto, el numero es ",num)