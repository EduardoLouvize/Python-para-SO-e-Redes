import socket
import sys
import os

HOST = socket.gethostname()
PORTA = 8881


# Imprime o status de download
def imprime_status(bytes, tam):
    kbytes = bytes/1024
    tam_bytes = tam/1024
    texto = "Baixando... "
    texto = texto + "{:<.2f}".format(kbytes) + " KB "
    texto = texto + "de " + "{:<.2f}".format(tam_bytes) + " KB"
    print(texto)


# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nome_arquivo = input("Entre com o nome do arquivo: ")
nome, extensao = nome_arquivo.split(".")
nome_arquivo_destino = nome + "_arquivo_recebido." + extensao
nome_arquivo = os.path.join(sys.path[0], nome_arquivo)
try:
    # Tenta se conectar ao servidor
    s.connect((HOST, PORTA))
    # Envia o nome do arquivo
    s.send(nome_arquivo.encode("ascii"))
    # Recebe o tamanho do arquivo
    msg = s.recv(12)
    tamanho = int(msg.decode("ascii"))
    # Checa se o arquivo existe no servidor:
    if (tamanho != -1):
        # Gera o arquivo local na pasta download
        arq = open(nome_arquivo_destino, "wb")
        soma = 0
        bytes = s.recv(4096)
        # Escreve o arquivo
        while bytes:
            arq.write(bytes)
            # Impressão do status de download
            soma = soma + len(bytes)
            os.system("cls")
            imprime_status(soma, tamanho)
            bytes = s.recv(4096)
        # Fecha o arquivo
        arq.close()
    else:
        print(f"Erro: arquivo {nome_arquivo} não encontrado no servidor!")
except Exception as erro:
    print(str(erro))
# Fecha o socket
s.close()
