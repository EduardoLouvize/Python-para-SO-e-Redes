# Escreva uma função em Python que, dado um número PID, imprima o nome do usuário proprietário, o tempo de criação e o
# uso de memória em KB.
import psutil
import time

pids = psutil.pids()

pid = pids[len(pids)-1]
processo = psutil.Process(pid)

print(f"Processo: {processo.name()}")
print(f"Proprietário: {processo.username()}")
print(f"Tempo de criação: {time.ctime(processo.create_time())}")
print(f"Uso de memória (RSS): {processo.memory_info().rss} KB")
