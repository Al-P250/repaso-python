import socket as sk
import time

sock=sk.socket(sk.AF_INET, sk.SOCK_STREAM)

sock.connect(("127.0.0.1", 12500))

salir=False
while not salir:
    mensaje= input("Introduce el mensaje que le quieres enviar al servidor (o escribe 'salir'): \n")
    sock.send(mensaje.encode())
    print("El mensaje está enviado")
    time.sleep(1)
    if mensaje=="salir":
        salir=True