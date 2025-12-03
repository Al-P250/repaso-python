import socket as sk
import time

conexion=sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
salir=False
while not salir:
    mensaje= input("Introduce el mensaje que le quieres enviar al servidor (o escribe 'salir'): \n")
    conexion.sendto(mensaje.encode(), ("127.0.0.1", 5000))
    print("El mensaje está enviado")
    time.sleep(1)
    if mensaje=="salir":
        salir=True