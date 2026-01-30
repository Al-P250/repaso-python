import random
import random as r

from veintiuna.carta import Carta

manoJugador=[]
manoCasa=[]
def verAses(mano):
    for carta in mano:
        if sumarCartas(mano)>21 and carta.valor==11:
            carta.valor=1

def sacarCarta(mano,baraja,veces):
    for i in range(veces):
        ultimaCarta=baraja.poblacion()
        mano.append(ultimaCarta)
    verAses(mano)

def sumarCartas(mano):
    total=0
    for carta in mano:
        total += carta.valor
    return total



def llamarBaraja():
    baraja=[]
    palos=["espadas","oros", "copas", "bastos"]
    for i in range(4):
        for j in range(1, 11):
            if j==1:
                carta=Carta("As", 11,palos[i])
            elif j<8:
                carta=Carta(j,j,palos[i])
            else:
                figuras=["Sota", "Caballo", "Rey"]
                carta=Carta(figuras[j-8],10,palos[i])
            baraja.append(carta)
    return baraja

baraja=llamarBaraja()
random.shuffle(baraja)
for carta in baraja:
    print(carta)
    print(f"El valor de la carta es {carta.valor}")

sacarCarta(manoCasa,baraja,3)
for i in range(len(manoCasa)):
    print(manoCasa[i])
    print(manoCasa[i].valor)


sacarCarta(manoJugador,baraja,3)
for i in range(len(manoJugador)):
    print(manoJugador[i])
    print(manoJugador[i].valor)
