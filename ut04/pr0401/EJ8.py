from random import *
i = 0
vJugador = 0
vMaquina = 0
opciones = ["piedra","papel","tijeras","lagarto","spock"]
while(vJugador < 5 and vMaquina < 5):
    jugador = input("Eleccion del jugador: ").lower()
    num = randint(0,4)
    maquina = opciones[num]
    print("Maquina elige: ",maquina)
    match jugador:
        case "piedra":
            if maquina in ['lagarto', 'tijeras']:
                vJugador = vJugador +1
                print("gana el jugador") 
            elif maquina in ['papel', 'spock']:
                vMaquina = vMaquina +1
                print("Gana la maquina")
            else:
                print("Empate")
        case "papel":
            if maquina in ['piedra', 'spock']:
                vJugador = vJugador +1
                print("gana el jugador") 
            elif maquina in ['lagarto', 'tijeras']:
                vMaquina = vMaquina +1
                print("Gana la maquina")
            else:
                print("Empate")
        case "tijera":
            if maquina in ['lagarto', 'papel']:
                vJugador = vJugador +1
                print("gana el jugador") 
            elif maquina in ['piedra', 'spock']:
                vMaquina = vMaquina +1
                print("Gana la maquina")
            else:
                print("Empate")
        case "lagarto":
            if maquina in ['spock', 'papel']:
                vJugador = vJugador +1
                print("gana el jugador") 
            elif maquina in ['piedra', 'tijeras']:
                vMaquina = vMaquina +1
                print("Gana la maquina")
            else:
                print("Empate")
        case "spock":
            if maquina in ['piedra', 'tijeras']:
                vJugador = vJugador +1
                print("gana el jugador") 
            elif maquina in ['papel', 'lagarto']:
                vMaquina = vMaquina +1
                print("Gana la maquina")
            else:
                print("Empate")
    print("Victorias del jugador: ", vJugador)
    print("Victoias de la maquina: ",vMaquina)
if(vJugador < vMaquina):
    print("Gana la maquina")
else:
    print("Gana el jugador")