import socket as sk

conexion=sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
conexion.bind(("127.0.0.1",5000))

print("Este recibidor está escuchando en el puerto 5000.")

while True:
    datos, direccion =conexion.recvfrom(1024)
    print(f"De la dirección {direccion} llega la siguiente información: \n {datos.decode()}")