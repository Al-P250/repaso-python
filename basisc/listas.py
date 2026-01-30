import random as r

cosas=[]


def darPista(nombre):
    posicion=r.randint(0,len(nombre)-1)
    for cosa in cosas:
        while cosa==posicion:
            posicion = r.randint(0, len(nombre) - 1)

    cosas.append(posicion)
    letra=nombre[posicion]
    print("_"*posicion+letra,"_"*(len(nombre)-posicion-1))

numNomb=int(input("Introduzca la cantidad de nombres(min 5): "))
nombres=[]
while numNomb<5:
    numNomb=int(input("Mínimo 5, subnormal: "))
for i in range(numNomb):
    nombres.append(input("Introduzca un nombre: "))

aleatorio=nombres[r.randint(0,len(nombres)-1)]

vidas=len(aleatorio)
seguir=True

while vidas !=0 and seguir:
    adivinar=input("Adivina el nombre ")
    if adivinar==aleatorio:
        seguir=False
    else:
        vidas -= 1
        if vidas>0:
            """letra = r.randint(0, len(aleatorio)-1)
            print(f"La {letra+1} letra es {aleatorio[letra]}")"""
            darPista(aleatorio)

        else:
         print("Fallaste")


