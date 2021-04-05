import socket
import pickle

HOST = socket.gethostname()
PORTA = 8881

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

pasta = input("Informe o diretório a ser verificado: ")


try:
    # Tenta se conectar ao servidor
    s.connect((HOST, PORTA))
    # Envia o nome do arquivo
    s.send(pasta.encode("utf-8"))
    bytes = s.recv(100000)
    info = pickle.loads(bytes)
    if info:
        for i in info:
            print(i)
except Exception as erro:
    print(str(erro))
# Fecha o socket
s.close()
