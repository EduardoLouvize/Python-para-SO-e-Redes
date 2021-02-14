# Escreva um programa em Python usando o módulo ‘psutil’, que imprima para a partição corrente:
# a. o nome do dispositivo,
# b. o tipo de sistema de arquivos que ela possui (FAT, NTFS, EXT, ...),
# c. o total de armazenamento em GB e
# d. o armazenamento disponível em GB.
import psutil
print(psutil.disk_partitions())

particao_corrente = psutil.disk_partitions()[0]
print(f"Nome: {particao_corrente[0]}")
print(f"Sistema de arquivos: {particao_corrente[2]}")
print(f"Espaço livre: {round(psutil.disk_usage(particao_corrente[0]).total / (pow(2, 30)), 2)} GB")
print(f"Espaço livre: {round(psutil.disk_usage(particao_corrente[0]).free / (pow(2, 30)), 2)} GB")
