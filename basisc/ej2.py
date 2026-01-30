import random as r

from ayudita import printMatrix

matrz=[]
for i in range(4):
    matrz.append([])
    for j in range(4):
        matrz[i].append(r.randint(0,9))

printMatrix(matrz)

fila=0
columna=0
for i in range(len(matrz)):
    fila = 0
    columna = 0

    for j in range(len(matrz)):
        fila+=matrz[i][j]
        columna+=matrz[j][i]
    print(f"La suma de la {i+1} fila es {fila}")
    print(f"La suma de la {i+1} columna es {columna}")

