import socket
import pickle
import os
import funcoes_auxiliares as fa


# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Obtém o nome da máquina
host = socket.gethostname()
porta = 8881
# Associa a porta
socket_servidor.bind((host, porta))
# Escutando...
socket_servidor.listen()
print("Servidor de nome", host.upper(), "esperando conexão na porta", porta)
while True:
    # Aceita alguma conexão
    (socket_cliente, addr) = socket_servidor.accept()
    print("Conectado a:", str(addr))
    msg = socket_cliente.recv(100000)
    pasta = msg.decode("utf-8")
    conteudo_pasta = os.listdir(pasta)
    lista_arquivos = fa.listar_arquivos(pasta)
    info_bytes = pickle.dumps(lista_arquivos)
    socket_cliente.send(info_bytes)

    # Fecha o socket cliente
    socket_cliente.close()
# Fecha o socket servidor
socket_servidor.close()
