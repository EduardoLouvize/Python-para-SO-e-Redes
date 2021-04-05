import socket
import pickle
import time

# Endereco IP do Servidor
HOST = socket.gethostname()
# Porta que o Servidor está esperando
PORT = 5000
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_cliente.settimeout(5)
destino = (HOST, PORT)
for i in range(0, 5):
    try:
        msg = "1"
        socket_cliente.sendto(msg.encode('ascii'), destino)
        bytes = socket_cliente.recv(1024)
        if bytes:
            info = pickle.loads(bytes)
            print(time.ctime())
            print(info)
            break
    except socket.timeout:
        print("Sem resposta...")
        pass
socket_cliente.close()
