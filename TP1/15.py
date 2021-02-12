# Escreva uma função em Python que, dado um número PID, imprima o nome do usuário proprietário, o tempo de criação e o
# uso de memória em KB.
import psutil
import time


pid = 638080
processo = psutil.Process(pid)

print(f"Processo: {processo.name()}"
      f" | Proprietário: {processo.username()}"
      f" | Tempo de criação: {time.ctime(processo.create_time())}"
      f" | Uso de memória: {processo.memory_info()}")
