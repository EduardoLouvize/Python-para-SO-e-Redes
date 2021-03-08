import socket
import psutil

# Informações de armazenamento
hd = psutil.disk_usage("/")
hd_total_gb = (round((hd.total / (2**30)), 2))
hd_disponivel_gb = (round((hd.free / (2**30)), 2))


HOST = socket.gethostname()
PORT = 9991
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destino = (HOST, PORT)
msg = str(f"Armazenamento total: {hd_total_gb} Gb\n"
          f"Amazenamento Disponível: {hd_disponivel_gb} Gb\n")
socket_cliente.sendto(msg.encode('utf-8'), destino)
socket_cliente.close()
