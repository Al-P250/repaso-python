'''Un documento CSV hecho por IA con preguntas y respuestas y otro de jugadores.csv donde se guardan, efectivamente, los jugadores. Los jugadores se registran con nombre. Si ya existe, sigue con la partida según estaba. Si no existe empieza de cero. Al final de la partida, dice el número de aciertos y fallos. Si has terminado la partida e introduces el mismo nombre avisas de que se reinicia la àrtida. Si introduces el nombre "ranking" te muestra, efectivamente, el ranking. El ranking de jugadores que han terminado. Para trastornados mentales hacer que las preguntas sean aleatorias'''




import os.path


def addRowToCSV(tupla,rutaFichero):
    info=""
    for i in range(len(tupla)-1):
        info +=f"{tupla[i]},"
    info +=f"{tupla[-1]}\n"
    with open(rutaFichero, "a") as f:
        f.write(info)

def createRow(rutaParaLeer):
    tupla=[]
    try:
        titulo=input("¿Qué título quieres añadir? ")
        if titulo.isnumeric() or titulo=="":
            raise ValueError("El título no puede ser un número o un espacio vacío")
        with open(rutaParaLeer, "r") as f:
            cosas=[]
            validez=["titulo", "autor", "editorial", "genero", "paginas"]
            proseguir=True
            while proseguir:
                campo=input("Añada un campo para añadir a favoritos ")
                if validez.count(campo)==1:
                    cosas.append(campo)
                    if input("¿Quiere añadir algún campo más? ")=="N":
                        proseguir=False
                else:
                    raise ValueError("Ese campo no existe")
            for libro in f:
                valores=libro.split(",")
                if titulo==valores[0]:
                    for i in range(len(validez)):
                        if cosas.count(validez[i])==1:
                            tupla.append(valores[i])
    except ValueError as e:
        print(e)
        tupla.clear()
    return tupla


rutaFichero="librosFavoritos.csv"
rutaParaLeer="libros.csv"

if os.path.exists(rutaFichero):
    seguir=True
    while seguir:
        tupla=createRow(rutaParaLeer)
        if len(tupla)==0:
            print("Error")
        else:
            addRowToCSV(tupla,rutaFichero)
        if input("¿Quiere añadir algo más? ")=="N":
            seguir=False
else:
    open(rutaFichero, "x")