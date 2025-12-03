from estructuras_de_datos.perro import Perro

variable=""
tupla=(1,2,3)
lista=[]
diccionario={}

perrito=Perro("Tomasito", 4, 2000)
print(perrito)
print(perrito.nombre)
print(perrito.edad)
print(perrito.raza)

perrito.comer(300)
perrito.cagar(200)