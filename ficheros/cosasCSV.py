'''1.	Crear, si no existe ya, un archivo csv de algo que os interese.
2.	Gestionar la creación de nuevas tuplas.
3.	Acceder a un dato de una tupla.

Split()'''
import os.path


def addRowToCSV(tupla,rutaFichero):
    info=""
    for i in range(len(tupla)-1):
        info +=f"{tupla[i]},"
    info +=f"{tupla[-1]}\n"
    with open(rutaFichero, "a") as f:
        f.write(info)

def createRow():
    tupla=[]
    try:
        titulo=input("Introduzca un título: ")
        if titulo.isnumeric() or titulo=="":
            raise ValueError("El título no puede ser un número o un espacio en blanco")
        tupla.append(titulo)
        autor=input("Introduzca un autor: ")
        if autor.isnumeric() or autor=="":
            raise ValueError("El autor no puede ser un número o un espacio en blanco")
        tupla.append(autor)
        editorial=input("Introduzca una editorial: ")
        if editorial.isnumeric() or editorial=="":
            raise ValueError("La editorial no puede ser un número o un espacio en blanco")
        tupla.append(editorial)
        genero=input("Introduzca un género: ")
        if genero.isnumeric() or genero=="":
            raise ValueError("El género no puede ser un número o un espacio en blanco")
        tupla.append(genero)
        paginas=int(input("Introduzca el número de páginas: "))
        tupla.append(paginas)
    except ValueError as e:
        print(e)
        tupla.clear()
    return tupla


rutaFichero="libros.csv"


if os.path.exists(rutaFichero):
    seguir=True
    while seguir:
        tupla=createRow()
        if len(tupla)==0:
            print("Error")
        else:
            addRowToCSV(tupla,rutaFichero)
        if input("¿Quiere añadir algo más? ")=="N":
            seguir=False
else:
    open(rutaFichero, "x")
