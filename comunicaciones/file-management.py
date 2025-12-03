import socket as sk

def escribirArchivo(contenido):
    with open("archivo.txt", "a") as f:
        f.write(contenido)

puerto=25252
escribirArchivo("Grabación")

sock=sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
sock.bind(("127.0.0.1", puerto))
print(f"Este recibidor está escuchando en el puerto {puerto}")

while True:
    datos,direccion=sock.recvfrom(1024)
    info="\nEscrito por "+ str(direccion)
    info+="\n"+ datos.decode()
    escribirArchivo(info)