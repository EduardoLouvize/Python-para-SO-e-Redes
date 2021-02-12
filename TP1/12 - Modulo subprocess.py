# Indique uma maneira de criar um processo externo ao seu programa usando o módulo ‘os’ e usando o módulo ‘subprocess’
# de Python. Dê um exemplo de cada.

import subprocess

nome_arquivo = "arquivo_teste.txt"

subprocess.Popen(["notepad", nome_arquivo])
