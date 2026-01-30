import openpyxl

workbook=openpyxl.load_workbook("segundo.xlsx")
notas=workbook["Notas"]
print(notas)
ejercicios= notas["A1":"E4"]
print(ejercicios)

for fila in ejercicios:
    for celda in fila:
        print(celda.coordinate, celda.value)
    print("Final de la fila")

columna=notas.columns[1]