from ayudita import printMatrix

matriz=[]
lon=int(input("Introduzca el tamaño: "))

for i in range(lon):
    matriz.append([])
    for j in range(lon):
        if j==lon-i-1:
            matriz[i].append(1)
        else:
            matriz[i].append(0)


printMatrix(matriz)