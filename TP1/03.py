# Escreva um programa usando o módulo ‘os’ de Python que imprima o PID do próprio processo e também seu GID
# (identificador de grupo) caso seja sistema do tipo Linux.
import os

print(f"O PID do próprio processo é: {os.getpid()}")
sistema_operacional = os.name

if sistema_operacional == "posix":
    print(f"GID: {os.getgid()}")
