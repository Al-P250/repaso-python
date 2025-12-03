import copy
import random




def dibujarMapa(m):
   x=3
   for i in range(len(m)-1,-1,-1):
       print(f"{x}: {m[i]}")
       x-=1
   print("     0     1     2     3     4")


def generarItems(m):
   mina="💣"
   tesoro="🍩"
   coordsMina=(random.randint(0,4), random.randint(0,3))
   coordsTesoro=coordsMina
   while coordsMina==coordsTesoro:
       coordsTesoro=(random.randint(0,4), random.randint(0,3))
   m[coordsMina[1]][coordsMina[0]]=mina
   m[coordsTesoro[1]][coordsTesoro[0]]=tesoro
   return coordsMina,coordsTesoro


def cavar(m,m2):
   pala = "⛏️"
   print("Introduce las coordenadas de donde quieres cavar")
   coords=int(input("X: ")),(int(input("Y: ")))
   m[coords[1]][coords[0]]=pala
   m2[coords[1]][coords[0]]=pala
   return coords


mapa=[["  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  "]]
mapaVacio=copy.deepcopy(mapa)


dibujarMapa(mapaVacio)
coordsMina,coordsTesoro=generarItems(mapa)


fin =False
while not fin:
   coordsCavar=cavar(mapaVacio,mapa)
   if coordsCavar==coordsTesoro:
       print("Has ganado!")
       dibujarMapa(mapa)
       fin=True
   elif coordsCavar==coordsMina:
       print("Has perdido!")
       dibujarMapa(mapa)
       fin=True
   else:
       if coordsCavar[0]==coordsMina[0] and coordsCavar[1]+1==coordsMina[1] or coordsCavar[0]==coordsMina[0] and coordsCavar[1]-1==coordsMina[1] or coordsCavar[1]==coordsMina[1] and coordsCavar[0]+1==coordsMina[0] or coordsCavar[1]==coordsMina[1] and coordsCavar[0]-1==coordsMina[0] or coordsCavar[1]+1==coordsMina[1] and coordsCavar[0]+1==coordsMina[0] or coordsCavar[1]-1==coordsMina[1] and coordsCavar[0]+1==coordsMina[0] or coordsCavar[1]+1==coordsMina[1] and coordsCavar[0]-1==coordsMina[0] or coordsCavar[1]-1==coordsMina[1] and coordsCavar[0]-1==coordsMina[0] :
           print("Tienes una bomba cerca")
       dibujarMapa(mapaVacio)
