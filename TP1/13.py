# Usando o módulo ‘subprocess’ de Python, crie um processo externo e imprima o PID dele.

import subprocess

processo = subprocess.Popen("calc")
print(f"O PID do processo é: {processo.pid}")
