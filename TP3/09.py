import socket

HOST = socket.gethostname()
PORTA = 9991
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORTA)
socket_servidor.bind(orig)
print("Servidor", HOST.upper(), "esperando conexão na porta", PORTA)
(msg, cliente) = socket_servidor.recvfrom(1024)
print(msg.decode("utf-8"))
socket_servidor.close()
input('Pressione qualquer tecla para sair...')