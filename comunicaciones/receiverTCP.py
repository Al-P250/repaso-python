import socket as sk


sock=sk.socket(sk.AF_INET, sk.SOCK_STREAM)
sock.bind(("127.0.0.1",12500))

sock.listen(1)
print("El recibidor está esperando...")

connection, direction=sock.accept()
print(f"Conectado con {direction}, con {connection}")

print("Este recibidor está escuchando en el puerto 5000.")

salir=False
while not salir:
    datos =connection.recv(1024)
    if not datos:
        salir=True
    print(f"Llega la siguiente información: \n {datos.decode()}")