# Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de armazenamento disponível há
# na partição do sistema (onde o sistema está instalado).
import psutil


print(f"Espaço livre: {round(psutil.disk_usage('c:').free / (pow(2, 30)), 2)} GB")
