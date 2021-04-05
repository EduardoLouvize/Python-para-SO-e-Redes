import socket
import pickle
import time
import funcoes_auxiliares as fa

# Endereco IP do Servidor
HOST = socket.gethostname()
# Porta que o Servidor está esperando
PORTA = 5000
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORTA)
socket_servidor.bind(orig)
print("Servidor", HOST.upper(), "esperando conexão na porta", PORTA)
while True:
    try:
        (msg, cliente) = socket_servidor.recvfrom(1024)
        print(cliente)
        pedido_cliente = msg.decode("ASCII")
        if pedido_cliente == "1":
            time.sleep(6)
            resposta = fa.mostra_uso_memoria()
            resposta_bytes = pickle.dumps(resposta)
            print(f"{time.ctime()}... Enviando...")
            socket_servidor.sendto(resposta_bytes, cliente)
    except ConnectionResetError:
        print("Conexão encerrada")
socket_servidor.close()
