import shutil, os

"""Vas a crear un programa en Python que gestione archivos y carpetas para una supuesta aplicación de respaldo.
El programa debe hacer lo siguiente:

1. Comprobar si existe un directorio llamado Origen.
2. Si no existe, crearlo y generar dentro varios archivos de texto.
3. Leer el contenido de los archivos usando open().
Comprobar:
4. Si el nombre del archivo termina en .txt usando endswith()
5. Si una palabra clave (por ejemplo "backup") está contenida en el texto usando la cláusula in
6. Copiar archivos válidos a un directorio Respaldo usando shutil.copy
7. Copiar todo el directorio Respaldo a RespaldoTotal usando shutil.copytree
8. Cambia el nombre del archivo que contiene backup a importante.txt
9. Elimina los archivos no válidos con os.unlink"""


os.chdir("C:\\Users\\Usuario\\Documents\\Creación")

if not os.path.exists("Origen"):
    os.mkdir("Origen")
    if not os.path.exists("Origen/fileNuevo.txt"):
       open("C:\\Users\\Usuario\\Documents\\Creación\\Origen\\fileNuevo.txt","x")
    if not os.path.exists("Origen/novedad.txt"):
       open("C:\\Users\\Usuario\\Documents\\Creación\\Origen\\novedad.txt","x")
    if not os.path.exists("Origen/textoVacio.txt"):
       open("C:\\Users\\Usuario\\Documents\\Creación\\Origen\\textoVacio.txt","x")
    if not os.path.exists("Origen/cositas.txt"):
       open("C:\\Users\\Usuario\\Documents\\Creación\\Origen\\cositas.txt","x")

if not os.path.exists("Respaldo"):
    os.mkdir("../Respaldo")

archivos=os.listdir("Origen")

for archivo in archivos:
    if archivo.endswith(".txt"):
        with open(archivo, "r") as f:
            if "backup" in f.readline():
                shutil.copy(archivo, "../Respaldo")
                shutil.move(archivo, "importante.txt")


os.chdir("C:\\Users\\Usuario\\Documents\\Creación")
shutil.copytree("Respaldo","C:\\Users\\Usuario\\Desktop\\RespaldoTotal")


