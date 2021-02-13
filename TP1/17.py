# Escreva um programa em Python, usando o módulo ‘psutil’, que imprima 20 vezes, de segundo a segundo, o percentual do
# uso de CPU do computador.
import psutil
import time

for i in range(20):
    print(f"Medida {i+1}: {psutil.cpu_percent()}")
    time.sleep(1)
