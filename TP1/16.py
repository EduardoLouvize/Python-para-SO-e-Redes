# Escreva um programa em Python, usando o módulo ‘psutil’, que imprima o tempo de CPU em segundos por núcleo.
import psutil

tempos = psutil.cpu_times(percpu=True)
print("Tempos de CPU em segundos:")
for i in range(0, len(tempos)):
    print(f"CPU {i+1}:")
    print(f"Modo usuário: {round(tempos[i].user, 3)} | "
          f"Modo de sistema: {round(tempos[i].system, 3)} | "
          f"Modo de espera: {round(tempos[i].idle, 3)}")

