ciclo = str(input("¿Qué ciclo estás estudiando?: "))
print (
    "Desarrollo de aplicaciones multiplataforma" if ciclo == "DAM" else
    "Desarrollo de aplicaciones web" if ciclo == "DAW" else
    "Administracion de sistemas en red" if ciclo == "ASIR" else
    "Ese ciclo no existe"
)